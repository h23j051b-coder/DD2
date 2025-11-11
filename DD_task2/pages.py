from otree.api import *
from .models import C
import json
import os
import time
from datetime import datetime, timezone

class Intro(Page):
    template_name = 'DD_task2/Intro.html'

class DelayPage(Page):
    form_model = 'player'
    form_fields = ['choice_data']

    def vars_for_template(self):
        eft_data = self.participant.vars.get('eft_data', [])

        # participant.vars に未保存なら JSON から読み込む
        if not eft_data:
            label = self.participant.label
            save_dir = os.path.join("C:/path/to/save", "eft_data")  # Day1 と同じ保存先
            filename = os.path.join(save_dir, f"{label}.json")

            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    eft_data = json.load(f)
            else:
                eft_data = []

            self.participant.vars['eft_data'] = eft_data

        # 現在ラウンドの遅延条件
        current_delay = self.player.delay

        # DD_task2のラウンド遅延条件に対応するEFT回答を検索
        eft = next((e for e in eft_data if e.get('delay') == current_delay), {})

        # 金額提示順
        if self.player.order_type == 'asc':
            amounts = C.AMOUNTS
        else:
            amounts = list(reversed(C.AMOUNTS))

        return dict(
            delay=current_delay,
            delayed_reward=C.DELAYED_REWARD,
            amounts=amounts,
            eft_goal=eft.get('goal'),
            eft_5w1h=eft.get('text_5w1h'),
            eft_emotion=eft.get('text_emotion'),
        )

    def before_next_page(self, timeout_happened=None):
        self.player.set_indifference_point()

        if self.round_number == C.NUM_ROUNDS:
            self.player.set_auc()


class EndPage(Page):
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS

    def vars_for_template(self):
        return dict(
            message="データを保存しました。",
            auc=self.player.auc,
        )

    def before_next_page(self, timeout_happened=None):
        self.player.set_scores()
        self.player.finish_time = datetime.now(timezone.utc).isoformat()


page_sequence = [Intro, DelayPage, EndPage]