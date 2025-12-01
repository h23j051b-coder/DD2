from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'delay_discount'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 7  # 遅延条件の数
    AMOUNTS = [100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500,
           4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000,
           8500, 9000, 9250, 9500, 9750, 9900, 10000]
    DELAYS = ['明日', '明後日', '1週間後', '2週間後', '1か月後', '6か月後', '2年後']
    DELAYED_REWARD = 10000


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            # choices 用の入れ物を初期化
            p.participant.vars.setdefault('choices', {'asc': {}, 'desc': {}})

            # 遅延条件ランダム
            if 'page_order' not in p.participant.vars:
                p.participant.vars['page_order'] = random.sample(C.DELAYS, len(C.DELAYS))

            p.delay = p.participant.vars['page_order'][p.round_number - 1]

            # ラウンドごとに order_type をランダムで決定
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
        import json

        data = json.loads(self.choice_data)
        amounts = data['amounts']
        choices = data['choices']  # "immediate" or "delayed"

        DEBUG = False

        if DEBUG:
            print("DEBUG set_indifference_point")
            print("amounts:", amounts)
            print("choices:", choices)
            print("order_type:", getattr(self, "order_type", None))

        # 特殊ケース：全部 delayed / 全部 immediate
        if all(c == 'delayed' for c in choices):
            ip = max(amounts)
        elif all(c == 'immediate' for c in choices):
            ip = min(amounts)
        else:
            ascending = amounts[0] < amounts[-1]

            if ascending:
                try:
                    first_immediate_idx = choices.index("immediate")
                except ValueError:
                    ip = min(amounts)
                else:
                    if first_immediate_idx == 0:
                        ip = min(amounts)
                    else:
                        prev_amt = amounts[first_immediate_idx - 1]
                        curr_amt = amounts[first_immediate_idx]
                        ip = (prev_amt + curr_amt) / 2.0

            else:
                last_immediate_idx = None
                for i in range(len(choices)-1, -1, -1):
                    if choices[i] == "immediate":
                        last_immediate_idx = i
                        break

                if last_immediate_idx is None:
                    ip = max(amounts)
                else:
                    if last_immediate_idx == len(amounts) - 1:
                        ip = min(amounts)
                    else:
                        next_amt = amounts[last_immediate_idx + 1]
                        curr_amt = amounts[last_immediate_idx]
                        ip = (curr_amt + next_amt) / 2.0

        self.indifference_point = ip
        self.participant.vars['choices'][self.order_type][self.delay] = ip

        if DEBUG:
            print("calculated ip:", ip)


    # ==========================
    #   AUC 計算（numpy不使用）
    # ==========================
    def set_auc(self):
        ips = [p.indifference_point for p in self.in_all_rounds()]  # 7つの IP

        max_val = C.DELAYED_REWARD  # 10000
        normalized_ips = [ip / max_val for ip in ips]

        n = len(ips)
        normalized_delays = [i / (n - 1) for i in range(n)]

        auc = 0
        for i in range(n - 1):
            auc += (normalized_ips[i] + normalized_ips[i + 1]) * (normalized_delays[i + 1] - normalized_delays[i]) / 2

        self.auc = auc


    def set_scores(self):
        """必要ならここに追加処理を書く。今は何もしない。"""
        pass
