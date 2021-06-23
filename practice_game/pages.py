from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
class PracticeGameInstruction(Page):
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


    def vars_for_template(self):
        return {
            'opinion_last_round': self.player.opinion_last_round,
            'observed_player1': self.player.observed_opinion_player1,
            'observed_player2': self.player.observed_opinion_player2,
            'last_round': self.round_number - 1,
            'if_connect_player1': self.player.if_connect_player1,
            'if_connect_player2': self.player.if_connect_player2,
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

        # self.participant.vars['neighbors_id_set'] = list(dict.fromkeys(self.participant.vars['neighbors_id_set']))
        self.participant.vars['neighbors_opinion_set'] = []
        for neighbor in self.participant.vars['neighbors_id_set']:
            self.participant.vars['neighbors_opinion_set'].append(self.participant.vars['others_last_opinions'][self.participant.vars['others_id_in_group'].index(neighbor)])
        self.player.num_neighbors = len(self.participant.vars['neighbors_opinion_set'])
        print(f'I am player {self.player.id_in_group}, my neighbors and their last round opinions are')
        print(self.participant.vars['neighbors_id_set'])
        print(self.participant.vars['neighbors_opinion_set'])

class OpinionUpdate(Page):
    form_model = 'player'
    form_fields = ['opinion_this_round']
    def vars_for_template(self):
        return {
            'opinion_last_round': self.player.opinion_last_round,
            'last_round': self.round_number - 1,
            'num_neighbors': self.player.num_neighbors,
            'neighbors_opinion_set': self.participant.vars['neighbors_opinion_set'],
        }

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def vars_for_template(self):
        return {
            'player_all_rounds': self.player.in_all_rounds(),
        }

page_sequence = [PracticeGameInstruction,GenerateInitialOpinionWaitPage, OpinionUpdateWaitPage, GenerateObservedPlayersWaitPage, NeighborUpdate, OpinionUpdate, Results]
