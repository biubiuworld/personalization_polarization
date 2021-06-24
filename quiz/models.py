from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'quiz'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question1 = models.IntegerField(choices=[(0, "2"), (1, "2 or 3"), (2, "1 or 2 or 3"), (3, "3")],
                                    label='As Player 1, if you see the true number is 1, which message might show up in the message menu?',
                                    widget=widgets.RadioSelectHorizontal)
