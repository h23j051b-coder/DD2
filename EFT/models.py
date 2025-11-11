from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'EFT'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 7
    DELAYS = ['明日', '明後日', '1週間後', '2週間後', '1か月後', '6か月後', '2年後']

    GOALS_RELATED = [
    "おばあちゃん家でお年玉をもらう",
    "道端で拾う",
    "スーパーの抽選で商品券が当たる",
    "母国に帰る留学生からもらう",
    "部屋の掃除をしていたら見つける",
    "大学の奨学金がまとめて振り込まれる",
    "地域振興会や市から給付金が振り込まれる",
    "古くなった貯金箱にたまたま残っていたのを見つける",
    "払った敷金の一部が戻ってくる",
    "SNSキャンペーンや懸賞に応募する"
    ]

    GOALS_UNRELATED = [
    "掃除をして，偶然無くしたものを見つける",
    "SNSでアップした写真が偶然バズる",
    "テレビで好きな映画が放送されているのを発見する",
    "散歩中新しくて雰囲気が良いお店を発見する",
    "いつも使うトイレが新しくなっている",
    "ふと立ち寄った店が思い出の店だった",
    "雨上がりの空にきれいな虹を見つける",
    "道端で猫がじゃれているのを見つける",
    "たっぷりお昼寝をする",
    "昔の親友から嬉しい連絡が来る"
    ]


    CHOICES_EFT_1 = [
        [1, 'まったくポジティブにならない'],
        [2, 'ほとんどポジティブにならない'],
        [3, 'あまりポジティブにならない'],
        [4, 'ややポジティブになる'],
        [5, 'ポジティブになる'],
        [6, '非常にポジティブになる']
    ]

    CHOICES_EFT_2 = [
        [1, 'まったく重要ではない'],
        [2, 'ほとんど重要ではない'],
        [3, 'あまり重要でない'],
        [4, 'やや重要である'],
        [5, '重要である'],
        [6, '非常に重要である']
    ]

    CHOICES_EFT_3 = [
        [1, 'まったく高まらない'],
        [2, 'ほとんど高まらない'],
        [3, 'あまり高まらない'],
        [4, 'やや高まる'],
        [5, '高まる'],
        [6, '非常に高まる']
    ]

    CHOICES_EFT_4 = [
        [1, 'まったく思い浮かばない'],
        [2, 'ほとんど思い浮かばない'],
        [3, 'あまり思い浮かばない'],
        [4, 'やや思い浮かぶ'],
        [5, 'よく思い浮かぶ'],
        [6, '非常によく思い浮かぶ']
    ]

    CHOICES_EFT_5 = [
        [1, 'まったく鮮明でない'],
        [2, 'ほとんど鮮明でない'],
        [3, 'あまり鮮明でない'],
        [4, 'やや鮮明である'],
        [5, '鮮明である'],
        [6, '非常に鮮明である']
    ] 


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            import random

            # 群割付（参加者間）
            p.participant.vars['group_type'] = random.choice(["関連", "無関連"])

            # 遅延期（参加者内ランダム順）
            delays = C.DELAYS.copy()
            random.shuffle(delays)
            p.participant.vars['delay_order'] = delays


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    goal = models.StringField(
        choices=[],
        label="",
        widget=widgets.RadioSelect
    )

    text_5w1h = models.LongStringField(label="")
    text_5w1h_len = models.IntegerField(initial=0)

    text_emotion = models.LongStringField(label="")
    text_emotion_len = models.IntegerField(initial=0)

    rating_valence = models.IntegerField(label="この出来事を思い浮かべると，どれくらいポジティブになりますか？", choices=C.CHOICES_EFT_1, widget=widgets.RadioSelectHorizontal)
    rating_importance = models.IntegerField(label="この出来事はあなたにとってどれくらい重要なものですか？", choices=C.CHOICES_EFT_2, widget=widgets.RadioSelectHorizontal)
    rating_arousal = models.IntegerField(label="この出来事を思い浮かべたとき，どれくらい気持ちが高まりますか？", choices=C.CHOICES_EFT_3, widget=widgets.RadioSelectHorizontal)
    rating_frequency = models.IntegerField(label="この出来事について，普段どれくらい頻繁に思い浮かべますか？", choices=C.CHOICES_EFT_4, widget=widgets.RadioSelectHorizontal)
    rating_vividness = models.IntegerField(label="この出来事はどれくらい鮮明に思い浮かびますか？", choices=C.CHOICES_EFT_5, widget=widgets.RadioSelectHorizontal)

    def set_lens(self):
        self.text_5w1h_len = len(self.text_5w1h)
        self.text_emotion_len = len(self.text_emotion)
    
    finish_time = models.StringField()
    total_rating = models.IntegerField(initial=0)
