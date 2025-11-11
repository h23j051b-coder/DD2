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


class Episode(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.session.config['name'] == 'day1'

    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        group = self.participant.vars['group_type']

        if group == "関連":
            choices = [(g, g) for g in C.GOALS_RELATED]
        else:
            choices = [(g, g) for g in C.GOALS_UNRELATED]

        form._fields['goal'].widget = widgets.RadioSelect()
        form._fields['goal'].choices = choices

        return form

    def get_form_fields(self):
        return [
            'goal',
            'text_5w1h',
            'text_emotion',
            'rating_valence',
            'rating_importance',
            'rating_arousal',
            'rating_frequency',
            'rating_vividness'
        ]

    def vars_for_template(self):
        delay = self.participant.vars['delay_order'][self.round_number-1]
        group = self.participant.vars['group_type']
        return dict(delay=delay, group=group)

    def before_next_page(self):
        self.player.set_lens()
        self.player.total_rating = (
            self.player.rating_valence +
            self.player.rating_importance +
            self.player.rating_arousal +
            self.player.rating_frequency +
            self.player.rating_vividness
        )

        if 'eft_data' not in self.participant.vars:
            self.participant.vars['eft_data'] = []

        current_delay = self.participant.vars['delay_order'][self.round_number - 1]

        self.participant.vars['eft_data'].append(dict(
            delay=self.participant.vars['delay_order'][self.round_number-1],
            goal=self.player.goal,
            text_5w1h=self.player.text_5w1h,
            text_emotion=self.player.text_emotion
        ))

        # ===== JSON にも保存 =====
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


page_sequence = [Intro, Episode, End]
