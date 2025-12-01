from otree.api import *
from .models import C   # ← これが必要！！
import json
import os
from datetime import datetime, timezone


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class DelayPage(Page):
    form_model = 'player'
    form_fields = ['choice_data']

    def is_displayed(self):
        return 1 <= self.round_number <= 7

    def vars_for_template(self):
        eft_data = self.participant.vars.get('eft_data', [])

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
            delayed_reward_str=f"{C.DELAYED_REWARD:,}",
            eft_goal=eft.get('goal', ''),
            eft_5w1h=eft.get('text_5w1h', ''),
            eft_emotion=eft.get('text_emotion', ''),
            amount_pairs=amount_pairs,
            amounts=json.dumps(amounts), # ←超重要
        )


class BreakPage(Page):
    def is_displayed(self):
        return self.round_number == 4


class EndPage(Page):
    def is_displayed(self):
        return self.round_number == 7

    def before_next_page(self, timeout_happened=None):
        self.player.finish_time = datetime.now(timezone.utc).isoformat()


page_sequence = [
    Intro,
    DelayPage,
    BreakPage,
    EndPage,
]

