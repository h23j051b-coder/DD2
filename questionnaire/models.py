from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    WAIT_TIME = 180  # 3分（秒）

    # --- BIS choices ---
    CHOICES_BIS = [
        [1, 'まったく当てはまらない'],
        [2, 'あまり当てはまらない'],
        [3, 'やや当てはまらない'],
        [4, 'やや当てはまる'],
        [5, 'かなり当てはまる'],
        [6, 'まさに当てはまる']
    ]

    # --- JACS choices ---
    CHOICES_JACS_1 = [
        [1, '他のことに集中するのが困難になる'],
        [2, 'しばらく後は気にしないようになる']
    ]
    CHOICES_JACS_2 = [
        [1, '時々、どうしても課題にとりかかれないときがある'],
        [2, 'たいてい，何の問題もなくやり通す']
    ]
    CHOICES_JACS_3 = [
        [1, '頻繁に休憩をとる必要があり、他の課題もやりたくなる'],
        [2, '長時間、同じ課題に打ち込むことが出来る']
    ]

    # --- K6 choices ---
    CHOICES_K6 = [
        [0, '全くない'],
        [1, '少しだけ'],
        [2, 'ときどき'],
        [3, 'たいてい'],
        [4, 'いつも']
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # --- BIS q1~q22 ---
    q1 = models.IntegerField(label="私は、仕事の計画を入念に立てる", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q2 = models.IntegerField(label="私は、何も考えずに物事を進める", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q3 = models.IntegerField(label="私は、すぐに決めてしまう", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q4 = models.IntegerField(label="私は、楽天的である", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q5 = models.IntegerField(label="私は、「細部まで気を配る」ことがない", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q6 = models.IntegerField(label="私は、前もって、十分に練った旅行計画を立てる", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q7 = models.IntegerField(label="私は、自制心がある", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q8 = models.IntegerField(label="私にとって、集中することは容易である", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q9 = models.IntegerField(label="私は、定期的にお金を貯めている", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q10 = models.IntegerField(label="私は、じっくりと考える", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q11 = models.IntegerField(label="私は、雇用の安定のために画策する", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q12 = models.IntegerField(label="私は、考えなしにものを言う", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q13 = models.IntegerField(label="私は、複雑な問題について考えるのが好きだ", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q14 = models.IntegerField(label="私は、まったく「衝動的」に行動する", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q15 = models.IntegerField(label="私は、問題の解決策を考えているとすぐ飽きる", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q16 = models.IntegerField(label="私は、突然の衝動にかられて行動する", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q17 = models.IntegerField(label="私は、常に考え方が安定している", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q18 = models.IntegerField(label="私は、衝動的に買い物をする", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q19 = models.IntegerField(label="私は、よく趣味を変える", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q20 = models.IntegerField(label="私は、稼いだ以上にお金を使う", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q21 = models.IntegerField(label="私は、思考するとき、しばしば、本質とは無関係なことを考えている", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)
    q22 = models.IntegerField(label="私は、劇場や映画館で何かを鑑賞しているとき，あるいは，講義を受けているとき、じっとしていられない", choices=C.CHOICES_BIS, widget=widgets.RadioSelectHorizontal)

    # --- JACS j1~j36 ---
    j1 = models.IntegerField(label="自分にとってとても大切なものなくしてしまい、どこを探しても見つからないとき", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j2 = models.IntegerField(label="ある事をすぐに終えなければならないとわかっているとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j3 = models.IntegerField(label="新しい、面白いゲームを習ったとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j4 = models.IntegerField(label="難しい問題を解決しなければならないとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j5 = models.IntegerField(label="特に何もすることがなく退屈なとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)    
    j6 = models.IntegerField(label="自分にとって大切な事に取り組んでいるとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j7 = models.IntegerField(label="ある試合でずっと負け続けているとき", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j8 = models.IntegerField(label="難しい問題に取り組む準備をしているとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j9 = models.IntegerField(label="とても良い映画を見ているとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j10 = models.IntegerField(label="新しい機械を買ったばかりで、うっかり床に落とし、修理できないほど壊れてしまった場合", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j11 = models.IntegerField(label="難しい問題を解決しなければならないとき", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j12 = models.IntegerField(label="何か楽しいこと（本を読んだりプロジェクトに取り組んだり）を長時間していて忙しいとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j13 = models.IntegerField(label="大切なことを話さなければならないのに、いくら探してもその人の家が見つからない場合", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j14 = models.IntegerField(label="思いがけない自由時間ができて、何をするか考えなければならないとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j15 = models.IntegerField(label="興味を惹かれる新聞記事を読んでいるとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j16 = models.IntegerField(label="買い物から帰って、代金を払いすぎたことに気づいたにも関わらず返金をしてもらえないことが分かったとき", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j17 = models.IntegerField(label="家でする仕事があったとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j18 = models.IntegerField(label="休暇で楽しく過ごしているとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j19 = models.IntegerField(label="自分の仕事が甚だしく不十分だったと言われたとき", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j20 = models.IntegerField(label="多くの重要な用事を抱え、全てをすぐに終わらせなければならないとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j21 = models.IntegerField(label="同僚のひとりが、会議で面白いトピックを提案したとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j22 = models.IntegerField(label="交通渋滞で、大切な約束を果たせなかったら", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j23 = models.IntegerField(label="心底やりたいことが二つあるが、その両方はできないとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j24 = models.IntegerField(label="面白い課題で忙しいとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j25 = models.IntegerField(label="自分にとっても重要なことなのに、うまくできそうにないとき", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j26 = models.IntegerField(label="重要だが不愉快なことに対処しなければならないとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j27 = models.IntegerField(label="パーティーである人と楽しくおしゃべりしているとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j28 = models.IntegerField(label="本当に落ち込んでしまったとき", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j29 = models.IntegerField(label="やるべき大きな課題に直面しているとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j30 = models.IntegerField(label="あるゲームで自分が他のプレイヤーよりはるかに調子が良いことに気づいたとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j31 = models.IntegerField(label="同じ日に失敗が重なったとき", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j32 = models.IntegerField(label="つまらない課題があるとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j33 = models.IntegerField(label="面白いものを読むとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    j34 = models.IntegerField(label="良い仕事をしようと全力で努めたが、全てうまくいかなかったとき", choices=C.CHOICES_JACS_1, widget=widgets.RadioSelectHorizontal)
    j35 = models.IntegerField(label="退屈で面白くない義務があるとき", choices=C.CHOICES_JACS_2, widget=widgets.RadioSelectHorizontal)
    j36 = models.IntegerField(label="学びたいと思っている新しいことについて勉強しようとしているとき", choices=C.CHOICES_JACS_3, widget=widgets.RadioSelectHorizontal)
    
    # --- K6 k1~k6 ---
    k1 = models.IntegerField(label="神経過敏に感じましたか", choices=C.CHOICES_K6, widget=widgets.RadioSelectHorizontal)
    k2 = models.IntegerField(label="絶望的だと感じましたか", choices=C.CHOICES_K6, widget=widgets.RadioSelectHorizontal)
    k3 = models.IntegerField(label="そわそわ、落ち着かなく感じましたか", choices=C.CHOICES_K6, widget=widgets.RadioSelectHorizontal)
    k4 = models.IntegerField(label="気分が沈み込んで、何が起こっても気が晴れないように感じましたか", choices=C.CHOICES_K6, widget=widgets.RadioSelectHorizontal)
    k5 = models.IntegerField(label="何をするにも骨折りだと感じましたか", choices=C.CHOICES_K6, widget=widgets.RadioSelectHorizontal)
    k6 = models.IntegerField(label="自分は価値のない人間だと感じましたか", choices=C.CHOICES_K6, widget=widgets.RadioSelectHorizontal)

    time_vas = models.FloatField(
        label="今の時間の流れはどのように感じましたか？",
        blank=True
    )
    
    # --- スコア集計用フィールド --- #
    bis_motor = models.FloatField(initial=0)
    bis_planlessness = models.FloatField(initial=0)
    bis_selfcontrol = models.FloatField(initial=0)
    bis_reflection = models.FloatField(initial=0)
    bis_total = models.FloatField(initial=0)

    jacs_fixation = models.FloatField(initial=0)
    jacs_hesitation = models.FloatField(initial=0)
    jacs_fickleness = models.FloatField(initial=0)
    jacs_total = models.FloatField(initial=0)

    k6_total = models.FloatField(initial=0)


    # --- BIS 得点計算 --- #
    def set_bis_scores(self):
        reverse_items = ['q1','q6','q7','q8','q9','q10','q11','q13','q17']
        bis_scores = {q: (7 - getattr(self, q)) if q in reverse_items else getattr(self, q)
                      for q in [f'q{i}' for i in range(1, 23)]}
        self.bis_motor = sum(bis_scores[q] for q in ['q2','q3','q4','q5','q12','q14','q16','q21'])
        self.bis_planlessness = sum(bis_scores[q] for q in ['q1','q6','q11','q17'])
        self.bis_selfcontrol = sum(bis_scores[q] for q in ['q7','q9','q18','q19','q20','q22'])
        self.bis_reflection = sum(bis_scores[q] for q in ['q8','q10','q13','q15'])
        self.bis_total = sum(bis_scores.values())


    # --- JACS 得点計算 --- #
    def set_jacs_scores(self):
        def score(q): return getattr(self, q) - 1  # 1→0点, 2→1点

        self.jacs_fixation = sum(score(q) for q in ['j19','j31','j22','j10','j7','j25','j34','j28','j13','j16','j1','j4'])
        self.jacs_hesitation = sum(score(q) for q in ['j35','j29','j26','j32','j17','j20','j11','j2','j5','j8','j14','j23'])
        self.jacs_fickleness = sum(score(q) for q in ['j33','j3','j24','j21','j9','j6','j36','j12','j15','j27','j18','j30'])
        self.jacs_total = self.jacs_fixation + self.jacs_hesitation + self.jacs_fickleness


    # --- K6 得点計算 --- #
    def set_k6_score(self):
        self.k6_total = sum(getattr(self, f'k{i}') for i in range(1, 7))


    # --- 総合 --- #
    def set_scores(self):
        self.set_bis_scores()
        self.set_jacs_scores()
        self.set_k6_score()
    
    finish_time = models.StringField()

