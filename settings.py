from os import environ

SESSION_CONFIGS = [
    dict(
       name='practice_game',
       display_name="Practice Game",
       num_demo_participants=3,
       app_sequence=['practice_game']
    ),
    # dict(
    #     name='game_VhFlH0',
    #     display_name="game_VhFlH0",
    #     num_demo_participants=3,
    #     app_sequence=['game_VhFlH0']
    # ),
    # dict(
    #     name='game_VhFmH0',
    #     display_name="game_VhFmH0",
    #     num_demo_participants=3,
    #     app_sequence=['game_VhFmH0']
    # ),
    # dict(
    #     name='game_VhFhH0',
    #     display_name="game_VhFhH0",
    #     num_demo_participants=3,
    #     app_sequence=['game_VhFhH0']
    # ),
    dict(
        name='game_VlFmH0',
        display_name="game_VlFmH0",
        num_demo_participants=3,
        app_sequence=['game_VlFmH0', 'game_VhFhH0']
    ),
    # dict(
    #     name='game_VhFmH10',
    #     display_name="game_VhFmH10",
    #     num_demo_participants=3,
    #     app_sequence=['game_VhFmH10']
    # ),
    # dict(
    #     name='game_VhFhH10',
    #     display_name="game_VhFhH10",
    #     num_demo_participants=3,
    #     app_sequence=['game_VhFhH10']
    # ),
    dict(
        name='quiz',
        display_name="quiz",
        num_demo_participants=1,
        app_sequence=['quiz']
    ),
    # dict(
    #     name='Experiment_Survey',
    #     display_name="Experiment_Survey",
    #     num_demo_participants=1,
    #     app_sequence=['Experiment_Survey']
    # ),
    # dict(
    #     name='game_VhFmH0',
    #     display_name="Pilot",
    #     num_demo_participants=3,
    #     app_sequence=['game_VhFmH0','game_VhFhH10', 'experiment_payment_dollar']
    # ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

ROOMS = [
    dict(
        name='practice_game',
        display_name="Pilot",
        participant_label_file='_rooms/participant_label.txt',
    ),
]
# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '#lv4bm0%xkc_ve22ycyfq4$h_e_#=u9@)&%v6vh^x(&6y7ych@'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
