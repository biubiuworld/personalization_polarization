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
    name_in_url = 'experiment_payment_dollar'
    players_per_group = None
    num_rounds = 1
    participation_fee = 4.00
    dollar_per_credit = 0.01
    endowment = 6.00

class Subsession(BaseSubsession):
    # def set_payoff(self):
    #     for p in self.get_players():
    #         # p.payoff_game1 = p.participant.vars['VhFmV0_game_payoff']
    #         print(p.participant.vars['VhFhH10_game_payoff'])
    #         p.payoff_game2 = p.participant.vars['VhFhV10_game_payoff']
    #         # p.payoff_experiment = p.payoff_game1 + p.payoff_game2
    #         p.payoff_experiment = p.payoff_game2
    #         p.payoff_experiment_dollar = round(p.payoff_experiment * Constants.players_per_group, 2)
    #         p.total_payoff_experiment_dollar = p.payoff_experiment_dollar + Constants.participation_fee
    pass
class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # payoff_game1 = models.CurrencyField()
    # payoff_game2 = models.CurrencyField()
    # payoff_experiment = models.CurrencyField()
    # payoff_experiment_dollar = models.FloatField()
    total_payoff_experiment_dollar = models.FloatField()