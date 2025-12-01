from otree.api import *
from .models import C
import json
import os
from datetime import datetime, timezone

class Intro(Page):
    template_name = 'DD_task2/Intro.html'

    def is_displayed(self):
        return self.round_number == 1


class DelayPage(Page):
    form_model = 'player'
    form_fields = ['choice_data']

    def vars_for_template(self):
        eft_data = self.participant.vars.get('eft_data', [])

        if not eft_data:
            label = self.participant.label
            save_dir = os.path.join("C:/path/to/save", "eft_data")
            filename = os.path.join(save_dir, f"{label}.json")

            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    eft_data = json.load(f)
            else:
                eft_data = []

            self.participant.vars['eft_data'] = eft_data

        current_delay = self.player.delay
        eft = next((e for e in eft_data if e.get('delay') == current_delay), {})

        if self.player.order_type == 'asc':
            amounts = C.AMOUNTS
        else:
            amounts = list(reversed(C.AMOUNTS))

        amounts_str = [f"{a:,}" for a in amounts]
        amount_pairs = list(zip(amounts, amounts_str))

        return dict(
            delay=current_delay,
            delayed_reward=C.DELAYED_REWARD,
            delayed_reward_str=f"{C.DELAYED_REWARD:,}",
            amount_pairs=amount_pairs,
            amounts=amounts,
            eft_goal=eft.get('goal'),
            eft_5w1h=eft.get('text_5w1h'),
            eft_emotion=eft.get('text_emotion'),
        )

    def before_next_page(self, timeout_happened=None):
        self.player.set_indifference_point()

        if self.round_number == C.NUM_ROUNDS:
            self.player.set_auc()


class BreakPage(Page):
    template_name = 'DD_task2/Break.html'

    def is_displayed(self):
        return self.round_number == 4


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


# 🔥 DelayPageのページを自動生成 + 途中で BreakPage 挿入
page_sequence = [Intro]

for i in range(C.NUM_ROUNDS):
    page_sequence.append(DelayPage)

    # ★ 4ページ目が終わったら休憩ページを表示
    if i == 3:
        page_sequence.append(BreakPage)

page_sequence.append(EndPage)
