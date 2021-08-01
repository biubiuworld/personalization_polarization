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
    name_in_url = 'Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    First_name = models.StringField(label='Your First Name')
    Last_name = models.StringField(label='Your Last Name')
    Email = models.StringField(label='Your UCSC email')
    Student_ID = models.IntegerField(label='Your UCSC student ID')
    Session_date = models.StringField(label='The session date you are attending (mm/dd/yyyy)')
    Participant_ID = models.StringField(
        label='Your participant ID (The participant ID is the user name in the Zoom chat room (e.g. leeps_x where x is a number). If you are not assigned and ID, fill in "show-up")')
    Venmo_ID = models.StringField(label='Your Venmo account ID (We will pay you in 48 hours after the session ends.)')
    Comments = models.LongStringField(
        label='Is there any part of the experiment that makes your confusing? Please give us some comments.')
    Strategy = models.LongStringField(
        label='How do you play this game? Please describe your strategy based on your role and the rules.')
