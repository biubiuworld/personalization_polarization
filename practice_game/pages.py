from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
class PracticeGameInstruction(Page):
    def is_displayed(self):
        return self.round_number == 1



class GenerateInitialOpinionWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 1
    wait_for_all_groups = True
    after_all_players_arrive = 'generate_initial_opinion'

class OpinionUpdateWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number > 1
    wait_for_all_groups = True
    after_all_players_arrive = 'update_opinion_eachround'

class GenerateObservedPlayersWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'generate_observed_players_eachround'


class OpinionUpdate(Page):
    form_model = 'player'
    form_fields = ['opinion_this_round']

    def vars_for_template(self):
        return {
            'opinion_last_round': self.player.opinion_last_round,
            'observed_player1': self.player.observed_player1,
            'observed_player2': self.player.observed_player2,
            'last_round': self.round_number - 1
        }




class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def vars_for_template(self):
        return {
            'player_all_rounds': self.player.in_all_rounds(),
        }

page_sequence = [PracticeGameInstruction,GenerateInitialOpinionWaitPage, OpinionUpdateWaitPage, GenerateObservedPlayersWaitPage, OpinionUpdate, Results]
