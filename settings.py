from os import environ

SESSION_CONFIGS = [
    # dict(
    #    name='Vlh0_game',
    #    display_name="Vlh0_game",
    #    num_demo_participants=9,
    #    app_sequence=['Vlh0_game']
    # ),   
    # dict(
    #    name='Vlh0_practice',
    #    display_name="Vlh0_practice",
    #    num_demo_participants=9,
    #    app_sequence=['Vlh0_practice']
    # ),  
    dict(
        name='Treatment4',
        display_name="Treatment4",
        num_demo_participants=9,
        app_sequence=['quiz','Vlh10_practice', 'Vlh10_game']
    ),
    # dict(
    #     name='Treatment3',
    #     display_name="Treatment3",
    #     num_demo_participants=9,
    #     app_sequence=['quiz','Vlh0_practice', 'Vlh0_game']
    # ),
    # dict(
    #     name='Treatment2',
    #     display_name="Treatment2",
    #     num_demo_participants=9,
    #     app_sequence=['quiz_VhFh','fHh10_practice', 'fHh10_game']
    # ),
    # dict(
    #     name='Treatment1',
    #     display_name="Treatment1",
    #     num_demo_participants=9,
    #     app_sequence=['quiz_VhFh','fHh0_practice', 'fHh0_game']
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
