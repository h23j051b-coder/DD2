from otree.api import *
from .models import C
import json
import os
import time
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

        # participant.vars に未保存なら JSON から読み込む
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

        eft = next(
            (e for e in eft_data if e.get('delay') == current_delay),
            {}
        )

        # 金額提示順
        if self.player.order_type == 'asc':
            amounts = C.AMOUNTS
        else:
            amounts = list(reversed(C.AMOUNTS))
