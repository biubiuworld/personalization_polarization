from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
class GameInstruction(Page):
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        self.participant.vars['neighbors_id_set'] = []


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
    # live_method = 'live_getselectedneighbor'

    # timeout_seconds = 10
    def vars_for_template(self):
        return {
            'opinion_last_round': self.player.opinion_last_round,
            'observed_player1': self.player.observed_opinion_player1,
            'observed_player2': self.player.observed_opinion_player2,
            'last_round': self.round_number - 1,
            'if_connect_player1': self.player.if_connect_player1,
            'if_connect_player2': self.player.if_connect_player2,
            'if_miss_neighbor_last_round': self.player.in_round(self.round_number-1).if_miss_neighbor if self.round_number>1 else None
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

        if (self.player.if_connect_player1 is None) | (self.player.if_connect_player2 is None):
            self.player.if_miss_neighbor = 1
        # print(f'I am player {self.player.id_in_group}, my neighbors and their last round opinions are')
        # print(self.participant.vars['neighbors_id_set'])
        # print(self.participant.vars['neighbors_opinion_set'])


class OpinionUpdate(Page):
    form_model = 'player'
    form_fields = ['opinion_this_round']
    # timeout_seconds = 10

    def vars_for_template(self):
        return {
            'opinion_last_round': self.player.opinion_last_round,
            'last_round': self.round_number - 1,
            'num_neighbors': self.player.num_neighbors,
            'neighbors_opinion_set': self.participant.vars['neighbors_opinion_set'],
            'if_miss_opinion_last_round': self.player.in_round(self.round_number - 1).if_miss_opinion if self.round_number>1 else None
        }

    def before_next_page(self):
        # print(self.player.opinion_this_round == 0)
        if (self.player.num_neighbors == 0) & (self.player.opinion_this_round != 0):
            self.player.payoff = -(self.player.opinion_this_round-self.player.opinion_last_round)*(self.player.opinion_this_round-self.player.opinion_last_round)*10000
        elif (self.player.num_neighbors > 0) & (self.player.opinion_this_round != 0):
            for neighbor_Opinion in self.participant.vars['neighbors_opinion_set']:
                self.player.payoff += (Constants.V-Constants.f*(self.player.opinion_this_round - neighbor_Opinion)*(self.player.opinion_this_round - neighbor_Opinion) - (1-Constants.f)*(self.player.opinion_this_round - self.player.opinion_last_round)*(self.player.opinion_this_round - self.player.opinion_last_round))*10000
        else:
            self.player.payoff = 0
        if (self.player.if_connect_player1 is None) | (self.player.if_connect_player2 is None):
            self.player.payoff = 0
        # If a subject didn't update opinion this round, use previous opinion instead.
        if self.player.opinion_this_round == 0:
            self.player.if_miss_opinion = 1
            self.player.opinion_this_round = self.player.opinion_last_round


class Results(Page):
    # def is_displayed(self):
    #     return self.round_number == Constants.num_rounds
    # timeout_seconds = 10

    def vars_for_template(self):
        return {
            'player_all_rounds': self.player.in_all_rounds(),
        }

page_sequence = [
    GameInstruction,
    GenerateInitialOpinionWaitPage,
    OpinionUpdateWaitPage,
    GenerateObservedPlayersWaitPage,
    NeighborUpdate,
    OpinionUpdate,
    Results]

