from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
class GameInstruction(Page):
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        self.participant.vars['neighbors_id_set'] = []
        self.participant.vars['practice_game_payoff'] = 0.


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


class NeighborUpdate(Page):
    form_model = 'player'
    form_fields = ['if_connect_player1', 'if_connect_player2']

    # timeout_seconds = 25
    def vars_for_template(self):
        return {
            'opinion_last_round': self.player.opinion_last_round,
            'observed_player1': self.player.observed_opinion_player1,
            'observed_player2': self.player.observed_opinion_player2,
            'last_round': self.round_number - 1,
            'if_connect_player1': self.player.if_connect_player1,
            'if_connect_player2': self.player.if_connect_player2,
            'neighbors_opinion_set': self.participant.vars['neighbors_opinion_set'] if self.round_number>1 else None,
            'num_neighbors': len(self.participant.vars['neighbors_opinion_set']) if self.round_number>1 else None,

        }

    def before_next_page(self):
        if (self.player.if_connect_player1 == 1) & (self.player.disconnect_with_player1 == 0):
            self.participant.vars['neighbors_id_set'].append(self.player.observed_id_player1)

        if (self.player.if_connect_player1 == 0) & (self.player.disconnect_with_player1 == 1):
            self.participant.vars['neighbors_id_set'].remove(self.player.observed_id_player1)

        if (self.player.if_connect_player2 == 1) & (self.player.disconnect_with_player2 == 0):
            self.participant.vars['neighbors_id_set'].append(self.player.observed_id_player2)

        if (self.player.if_connect_player2 == 0) & (self.player.disconnect_with_player2 == 1):
            self.participant.vars['neighbors_id_set'].remove(self.player.observed_id_player2)

        self.participant.vars['neighbors_opinion_set'] = []
        for neighbor in self.participant.vars['neighbors_id_set']:
            self.participant.vars['neighbors_opinion_set'].append(self.participant.vars['others_last_opinions'][self.participant.vars['others_id_in_group'].index(neighbor)])
        self.player.num_neighbors = len(self.participant.vars['neighbors_opinion_set']) #number of neighbors this round
        self.player.neighbors_id_set = ', '.join(map(str, self.participant.vars['neighbors_id_set']))
        self.player.neighbors_opinion_set = ', '.join(map(str, self.participant.vars['neighbors_opinion_set']))
        self.participant.vars['neighbors_opinion_set'].sort() #reorder neighbors' opinons from low to high
        if (self.player.if_connect_player1 is None) | (self.player.if_connect_player2 is None):
            self.player.if_miss_neighbor = 1

        if self.timeout_happened:
            self.player.timeout_choose_neighbors = 1



class OpinionUpdate(Page):
    form_model = 'player'
    form_fields = ['opinion_this_round']
    # timeout_seconds = 25

    def vars_for_template(self):
        return {
            'opinion_last_round': self.player.opinion_last_round,
            'last_round': self.round_number - 1,
            'num_neighbors': self.player.num_neighbors,
            'neighbors_opinion_set': self.participant.vars['neighbors_opinion_set'],

        }

    def before_next_page(self):

        if (self.player.num_neighbors == 0) & (self.player.opinion_this_round >= 0):
            self.player.payoff = -(self.player.opinion_this_round-self.player.opinion_last_round)*(self.player.opinion_this_round-self.player.opinion_last_round)
        elif (self.player.num_neighbors > 0) & (self.player.opinion_this_round >= 0):
            for neighbor_Opinion in self.participant.vars['neighbors_opinion_set']:
                self.player.payoff += (Constants.V-Constants.f*(self.player.opinion_this_round - neighbor_Opinion)*(self.player.opinion_this_round - neighbor_Opinion) - (1-Constants.f)*(self.player.opinion_this_round - self.player.opinion_last_round)*(self.player.opinion_this_round - self.player.opinion_last_round))
        else:
            self.player.payoff = 0
        if (self.player.if_connect_player1 is None) | (self.player.if_connect_player2 is None):
            self.player.payoff = 0
        # If a subject didn't update opinion this round, use previous opinion instead.
        if self.timeout_happened:
            self.player.timeout_update_opinion = 1

        if self.player.opinion_this_round < 0:
            self.player.if_miss_opinion = 1
            self.player.opinion_this_round = self.player.opinion_last_round

        self.participant.vars['practice_game_payoff'] += self.player.payoff
        self.player.game_payoff = self.participant.vars['practice_game_payoff']
class Results(Page):

    # timeout_seconds = 5

    def vars_for_template(self):
        return {
            'player_all_rounds': self.player.in_all_rounds(),
        }



class GamePayment(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return{
            'practice_game_payoff': self.participant.vars['practice_game_payoff'],
        }

page_sequence = [
    GameInstruction,
    GenerateInitialOpinionWaitPage,
    OpinionUpdateWaitPage,
    GenerateObservedPlayersWaitPage,
    NeighborUpdate,
    OpinionUpdate,
    Results,
    GamePayment,
]
