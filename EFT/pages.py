from otree.api import Page, widgets
from .models import C
import random
import time
from datetime import datetime, timezone
import os
import json


class Intro(Page):
    template_name = 'EFT/Intro.html'

    def is_displayed(self):
        return self.session.config['name'] == 'day1' and self.round_number == 1

    def before_next_page(self):
        import random

        if 'episode_goals' not in self.participant.vars:
            self.participant.vars['episode_goals'] = []

            for i in range(C.NUM_ROUNDS):

                if self.participant.vars['group_type'] == "関連":
                    lst = C.GOALS_RELATED.copy()
                else:
                    lst = C.GOALS_UNRELATED.copy()

                random.shuffle(lst)

                self.participant.vars['episode_goals'].append(dict(
                    goal=None,
                    delay=self.participant.vars['delay_order'][i],
                    related_list=lst
                ))



class Select(Page):
    form_model = 'player'
    form_fields = [f'goal_{i}' for i in range(1, 8)]

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        # 安全に取り出す
        episode_goals = self.participant.vars.get('episode_goals', [])
        group = self.participant.vars.get('group_type', None)

        # 画面に渡す形を整える（各要素に delay と related_list が入っている想定）
        # goal_list は index 1..7 に対応するリスト
        goal_list = []
        for idx, eg in enumerate(episode_goals, start=1):
            goal_list.append({
                'idx': idx,
                'delay': eg.get('delay'),
                'options': eg.get('related_list', [])
            })

        return dict(
            group=group,
            goal_list=goal_list
        )

    def before_next_page(self):
        # フォームから得た goal_1..goal_7 を participant.vars['episode_goals'] に保存（更新）
        if 'episode_goals' not in self.participant.vars:
            # 保険：初期化（通常は creating_session で作っている）
            self.participant.vars['episode_goals'] = [
                {'delay': d, 'related_list': [], 'goal': None} for d in self.participant.vars.get('delay_order', C.DELAYS)
            ]

        for i in range(1, 8):
            val = getattr(self.player, f'goal_{i}')
            # participant.vars 側に保存（存在すれば上書き、なければ append）
            try:
                self.participant.vars['episode_goals'][i-1]['goal'] = val
            except Exception:
                # 保険：長さが足りない場合作る
                while len(self.participant.vars['episode_goals']) < i:
                    self.participant.vars['episode_goals'].append({'delay': None, 'related_list': [], 'goal': None})
                self.participant.vars['episode_goals'][i-1]['goal'] = val


class Episode(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.session.config['name'] == 'day1'

    def get_form_fields(self):
        return [
            'text_5w1h',
            'text_emotion',
            'rating_valence',
            'rating_importance',
            'rating_arousal',
            'rating_frequency',
            'rating_vividness'
        ]

    def vars_for_template(self):
        index = self.round_number - 1
        eg = self.participant.vars.get('episode_goals', [None]*C.NUM_ROUNDS)[index]
        selected_goal = eg.get('goal') if eg else None
        delay = eg.get('delay') if eg else None
        group = self.participant.vars.get('group_type', None)

        return dict(
            delay=delay,
            group=group,
            selected_goal=selected_goal
        )

    def before_next_page(self):
        self.player.set_lens()

        # 合計スコア
        self.player.total_rating = (
            self.player.rating_valence +
            self.player.rating_importance +
            self.player.rating_arousal +
            self.player.rating_frequency +
            self.player.rating_vividness
        )

        # データ保存
        if 'eft_data' not in self.participant.vars:
            self.participant.vars['eft_data'] = []

        index = self.round_number - 1
        eg = self.participant.vars.get('episode_goals', [None]*C.NUM_ROUNDS)[index]
        current_goal = eg.get('goal') if eg else None
        current_delay = eg.get('delay') if eg else None

        self.participant.vars['eft_data'].append(dict(
            delay=current_delay,
            goal=current_goal,
            text_5w1h=self.player.text_5w1h,
            text_emotion=self.player.text_emotion
        ))

        # JSON 保存
        save_dir = os.path.join(self.session.config['participant_label_dir'], "eft_data")
        os.makedirs(save_dir, exist_ok=True)
        filename = os.path.join(save_dir, f"{self.participant.label}.json")

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.participant.vars['eft_data'], f, ensure_ascii=False, indent=2)


class End(Page):
    def is_displayed(self):
        return self.session.config['name'] == 'day1' and self.round_number == C.NUM_ROUNDS

    def before_next_page(self, timeout_happened=None):
        self.player.finish_time = datetime.now(timezone.utc).isoformat()
        self.participant.vars['day1_completed'] = True


page_sequence = [Intro, Select, Episode, End]
