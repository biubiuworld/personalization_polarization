from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ExperimentPayment(Page):

    def vars_for_template(self):
        return{
            'payoff_game1': self.participant.vars['VlFmH0_game_payoff'],
            'payoff_game2': self.participant.vars['VhFhH0_game_payoff'],
            'payoff_experiment': self.participant.vars['VlFmH0_game_payoff']+self.participant.vars['VhFhH0_game_payoff'],
            'payoff_experiment_dollar': round(float(self.participant.vars['VlFmH0_game_payoff']+self.participant.vars['VhFhH0_game_payoff'])*0.01,2),
            'total_payoff_experiment_dollar': round(round(float(self.participant.vars['VlFmH0_game_payoff']+self.participant.vars['VhFhH0_game_payoff'])*0.01,2)+Constants.participation_fee,2),
        }
    def before_next_page(self):
        self.player.total_payoff_experiment_dollar = round(round(float(self.participant.vars['VlFmH0_game_payoff']+self.participant.vars['VhFhH0_game_payoff'])*0.01,2)+Constants.participation_fee,2)


page_sequence = [ExperimentPayment]
