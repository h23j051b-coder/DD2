from otree.api import *
from .models import C
import json
import os
from datetime import datetime, timezone


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class DelayPage(Page):
    form_model = 'player'
    form_fields = ['choice_data']

    def vars_for_template(self):
        current_delay = self.player.delay
        if self.player.order_type == 'asc':
            amounts = C.AMOUNTS
        else:
            amounts = list(reversed(C.AMOUNTS))
        amounts_str = [f"{a:,}" for a in amounts]
        amount_pairs = zip(amounts, amounts_str)
        return dict(
            delay=current_delay,
            delayed_reward_str=f"{C.DELAYED_REWARD:,}",
            amount_pairs=amount_pairs,
            amounts=json.dumps(amounts),
        )

    def before_next_page(self, timeout_happened=None):
        self.player.set_indifference_point()
        if self.round_number == C.NUM_ROUNDS:
            self.player.set_auc()


class EndPage(Page):
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS

    def before_next_page(self, timeout_happened=None):
        self.player.finish_time = datetime.now(timezone.utc).isoformat()


page_sequence = [
    Intro,
    DelayPage,
    EndPage,
]
