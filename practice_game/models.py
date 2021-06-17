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
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'practice_game'
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
    def generate_initial_opinion(self):
        for p in self.get_players():
            p.initial_opinion = round(random.uniform(0, 1),
                                      2)  # generate a random 2-decimal number as the initial opinion
            p.opinion_last_round = p.initial_opinion

    def update_opinion_eachround(self):
        for p in self.get_players():
            p.opinion_last_round = p.in_round(p.round_number - 1).opinion_this_round

    def generate_observed_players_eachround(self):
        for p in self.get_players():
            others_last_opinions = []
            for other in p.get_others_in_subsession():
                others_last_opinions.append(other.in_round(p.round_number).opinion_last_round)
            observed_players_this_round = random.sample(others_last_opinions, 2)
            p.observed_player1 = observed_players_this_round[0]
            p.observed_player2 = observed_players_this_round[1]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    initial_opinion = models.FloatField(min=0, max=1)
    opinion_last_round = models.FloatField(min=0, max=1)
    opinion_this_round = models.FloatField(min=0, max=1, label='Please update your opinion in this round')
    observed_player1 = models.FloatField(min=0, max=1)
    observed_player2 = models.FloatField(min=0, max=1)




