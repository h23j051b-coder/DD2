from otree.api import *
import numpy as np
import random

class C(BaseConstants):
    NAME_IN_URL = 'delay_discount'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 7  # 遅延条件の数
    AMOUNTS = ['100', '250', '500', '750', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000', '4,500', '5,000', '5500', '6,000', '6,500', '7,000', '7,500', '8,000', '8,500', '9,000', '9,250', '9,500', '9,750', '9,900', '10,000']  # 即時報酬候補
    DELAYS = ['明日', '明後日', '1週間後', '2週間後', '1か月後', '6か月後', '2年後']  # 遅延日数
    DELAYED_REWARD = '10,000'  # 遅延報酬

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            # choices用の入れ物を初期化（asc/desc両方）
            p.participant.vars.setdefault('choices', {'asc': {}, 'desc': {}})

            # 遅延条件をランダム順で1回ずつ割り当て
            if 'page_order' not in p.participant.vars:
                p.participant.vars['page_order'] = random.sample(C.DELAYS, len(C.DELAYS))

            # 今のラウンドの遅延条件を設定
            p.delay = p.participant.vars['page_order'][p.round_number - 1]

            # 金額提示順（昇順 or 降順）をランダムに設定
            p.order_type = random.choice(['asc', 'desc'])

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    delay = models.StringField()
    order_type = models.StringField()
    choice_data = models.LongStringField()  # JSONで選択履歴保存
    indifference_point = models.FloatField()
    auc = models.FloatField()
    finish_time = models.StringField()

    def set_indifference_point(self):
        """昇順・降順ごとの等価点を算出"""
        import json
        data = json.loads(self.choice_data)
        amounts = data['amounts']
        choices = data['choices']  # 'immediate' or 'delayed' のリスト

        ip = None
        if self.order_type == 'asc':
            for i in range(1, len(choices)):
                if choices[i-1] == 'immediate' and choices[i] == 'delayed':
                    ip = (amounts[i-1] + amounts[i]) / 2
                    break
        else:
            for i in range(1, len(choices)):
                if choices[i-1] == 'delayed' and choices[i] == 'immediate':
                    ip = (amounts[i-1] + amounts[i]) / 2
                    break

        if ip is None:
            if all(c == 'immediate' for c in choices):
                ip = min(amounts)
            else:
                ip = max(amounts)

        self.indifference_point = ip
        self.participant.vars['choices'][self.order_type][self.delay] = ip

    def set_auc(self):
        """昇順・降順ごとにAUCを算出（全ラウンド終了時に呼び出す）"""
        delay_to_days = {
            '明日': 1, '明後日': 2, '1週間後': 7, '2週間後': 14,
            '1か月後': 30, '6か月後': 180, '2年後': 730,
        }

        auc_results = {}
        for order in ['asc', 'desc']:
            delay_ip = self.participant.vars['choices'][order]
            if not delay_ip:
                continue

            # 日数順にソート
            sorted_items = sorted(delay_ip.items(), key=lambda x: delay_to_days[x[0]])
            delays, ips = zip(*sorted_items)
            x = np.array([delay_to_days[d] for d in delays], dtype=float)
            x /= np.max(x)
            y = np.array(ips, dtype=float) / C.DELAYED_REWARD
            auc_results[order] = np.trapz(y, x)

        # 平均AUCを保存
        self.auc = np.nanmean(list(auc_results.values()))
