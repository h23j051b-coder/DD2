from otree.api import *
from .models import C, Player
import time
from datetime import datetime, timezone

# --- Pages --- #
class BIS(Page):
    form_model = 'player'
    form_fields = [f"q{i}" for i in range(1, 23)]  # q1～q22
    template_name = 'questionnaire/BIS.html'


class JACS(Page):
    form_model = 'player'
    form_fields = [f"j{i}" for i in range(1, 37)]  # j1～j36
    template_name = 'questionnaire/JACS.html'


class K6(Page):
    form_model = 'player'
    form_fields = [f"k{i}" for i in range(1, 7)]  # k1～k6
    template_name = 'questionnaire/K6.html'

class Wait(Page):
    def vars_for_template(self):
        # まず定数から待機時間を取得
        wait_time_seconds = C.WAIT_TIME

        # それをテンプレートに渡す
        return dict(
            instruction_text=(
                "これから一定時間座って待機していただきます。<br>"
                "待機時間中はスマホや時計などは見ないようにお願いします。<br>"
                "その後、その時間の流れをどのように感じたかをスライダーで回答してください。<br><br>"
                "<b>これ以降は全画面表示に切り替えてください。</b><br>"
                "下のボタンを押すと全画面モードになります。"
            ),
            wait_time_ms=wait_time_seconds * 1000,  # ← ミリ秒に変換して渡す
        )

class TimePerceptionVAS(Page):
    form_model = 'player'
    form_fields = ['time_vas']

    def vars_for_template(self):
        return dict(
            label_text="今の時間の流れはどのくらいに感じましたか？",
            left_label="非常に短く感じた",
            mid_label="普通",
            right_label="非常に長く感じた"
        )

class EndPage(Page):
    template_name = 'questionnaire/EndPage.html'

    def before_next_page(self, timeout_happened=None):
        self.player.set_scores()
        self.player.finish_time = datetime.now(timezone.utc).isoformat()


# ページの順番
page_sequence = [BIS, JACS, K6, Wait, TimePerceptionVAS, EndPage]
