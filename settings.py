from os import environ
import os

# --- Redis を使うための設定（追加） ---
REDIS_URL = environ.get("REDIS_URL")


SESSION_CONFIGS = [
    dict(
        name='day1',
        display_name='【Day1】質問紙 + 課題１，２',
        num_demo_participants=1,
        app_sequence=['questionnaire', 'EFT'],
        participant_label_dir='C:/path/to/save',
    ),
    dict(
        name='day2',
        display_name='【Day2】課題３',
        num_demo_participants=1,
        app_sequence=['DD_task2'],
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

# Day1・Day2 のデータ引き継ぎに使用
PARTICIPANT_FIELDS = [
    'group_type',
    'delay_order',
    'eft_data'
]

SESSION_FIELDS = []

LANGUAGE_CODE = 'ja'

REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = environ.get('OTREE_SECRET_KEY')

ROOMS = [
    dict(
        name='day1',
        display_name='Day1用ルーム',
        participant_label_file='_rooms/label.txt'
    ),
    dict(
        name='day2',
        display_name='Day2用ルーム',
        participant_label_file='_rooms/label.txt'
    ),
]

# oTree を本番モードに
os.environ['OTREE_PRODUCTION'] = '1'
DEBUG = False
