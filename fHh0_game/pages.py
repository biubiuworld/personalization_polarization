from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import math
class GameInstruction(Page):
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        self.participant.vars['neighbors_id_set'] = []
        self.participant.vars['game_payoff'] = 0.
        self.participant.vars['payoff_in_all_rounds'] = []

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
    form_fields = ['if_connect_player1', 'if_connect_player2', 'opinion_this_round', 'update_neighbor_opinion_1',
                   'update_neighbor_opinion_2', 'update_neighbor_opinion_3', 'update_neighbor_opinion_4',
                   'update_neighbor_opinion_5','update_neighbor_opinion_6','update_neighbor_opinion_7','update_neighbor_opinion_8',
                   'disconnect_with_neighbor_1', 'disconnect_with_neighbor_2', 'disconnect_with_neighbor_3', 'disconnect_with_neighbor_4', 'disconnect_with_neighbor_5',
                   'disconnect_with_neighbor_6', 'disconnect_with_neighbor_7', 'disconnect_with_neighbor_8']

    timeout_seconds = 90

    def vars_for_template(self):
        self.participant.vars['neighbors_opinion_set'] = []
        for neighbor in self.participant.vars['neighbors_id_set']:
            self.participant.vars['neighbors_opinion_set'].append(self.participant.vars['others_last_opinions'][self.participant.vars['others_id_in_group'].index(neighbor)])
        self.player.num_neighbors = len(self.participant.vars['neighbors_opinion_set'])
        if self.player.num_neighbors > 0:
            self.player.neighbor_opinion_1 = self.participant.vars['neighbors_opinion_set'][0]
        if self.player.num_neighbors > 1:
            self.player.neighbor_opinion_2 = self.participant.vars['neighbors_opinion_set'][1]
        if self.player.num_neighbors > 2:
            self.player.neighbor_opinion_3 = self.participant.vars['neighbors_opinion_set'][2]
        if self.player.num_neighbors > 3:
            self.player.neighbor_opinion_4 = self.participant.vars['neighbors_opinion_set'][3]
        if self.player.num_neighbors > 4:
            self.player.neighbor_opinion_5 = self.participant.vars['neighbors_opinion_set'][4]
        if self.player.num_neighbors > 5:
            self.player.neighbor_opinion_6 = self.participant.vars['neighbors_opinion_set'][5]
        if self.player.num_neighbors > 6:
            self.player.neighbor_opinion_7 = self.participant.vars['neighbors_opinion_set'][6]
        if self.player.num_neighbors > 7:
            self.player.neighbor_opinion_8 = self.participant.vars['neighbors_opinion_set'][7]
        return {
            'opinion_last_round': self.player.opinion_last_round,
            'observed_player1': self.player.observed_opinion_player1,
            'observed_player2': self.player.observed_opinion_player2,
            'last_round': self.round_number - 1,
            'if_connect_player1': self.player.if_connect_player1,
            'if_connect_player2': self.player.if_connect_player2,
            'neighbors_opinion_set': self.participant.vars['neighbors_opinion_set'] if self.round_number>1 else [],
            'neighbors_id_set': self.participant.vars['neighbors_id_set'] if self.round_number>1 else [],
            'num_neighbors': len(self.participant.vars['neighbors_opinion_set']) if self.round_number>1 else 0,
            'neighbor_opinion_1': self.player.neighbor_opinion_1,
            'neighbor_opinion_2': self.player.neighbor_opinion_2,
            'neighbor_opinion_3': self.player.neighbor_opinion_3,
            'neighbor_opinion_4': self.player.neighbor_opinion_4,
            'neighbor_opinion_5': self.player.neighbor_opinion_5,
            'neighbor_opinion_6': self.player.neighbor_opinion_6,
            'neighbor_opinion_7': self.player.neighbor_opinion_7,
            'neighbor_opinion_8': self.player.neighbor_opinion_8,
            'observed_id_player1': self.player.observed_id_player1,
            'observed_id_player2': self.player.observed_id_player2,
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

        self.player.neighbors_id_set_after_choose_neighbors = ', '.join(map(str, self.participant.vars['neighbors_id_set']))
        self.participant.vars['neighbors_opinion_set_after_choose_neighbors'] = []
        for neighbor in self.participant.vars['neighbors_id_set']:
            self.participant.vars['neighbors_opinion_set_after_choose_neighbors'].append(self.participant.vars['others_last_opinions'][self.participant.vars['others_id_in_group'].index(neighbor)])
        self.player.neighbors_opinion_set_after_choose_neighbors = ', '.join(map(str, self.participant.vars['neighbors_opinion_set_after_choose_neighbors']))
        
        #remove disconnected neighbors
        disconnection_checkbox = [self.player.disconnect_with_neighbor_1, self.player.disconnect_with_neighbor_2, self.player.disconnect_with_neighbor_3, self.player.disconnect_with_neighbor_4,
        self.player.disconnect_with_neighbor_5, self.player.disconnect_with_neighbor_6, self.player.disconnect_with_neighbor_7, self.player.disconnect_with_neighbor_8]
        all_neighbor_guess_set = [self.player.update_neighbor_opinion_1, self.player.update_neighbor_opinion_2, self.player.update_neighbor_opinion_3, self.player.update_neighbor_opinion_4,
        self.player.update_neighbor_opinion_5, self.player.update_neighbor_opinion_6, self.player.update_neighbor_opinion_7, self.player.update_neighbor_opinion_8]
        number_neighbors = len(self.participant.vars['neighbors_id_set']) #attention: number_neighbors is before neighbor disconnection
        disconnection_checkbox = disconnection_checkbox[:number_neighbors]
        delete_index = []
        self.participant.vars['neighbors_opinion_guess_set'] = [] 
        for i in range(0, number_neighbors):
            self.participant.vars['neighbors_opinion_guess_set'].append(all_neighbor_guess_set[i])
            if disconnection_checkbox[i] == 1:
                delete_index.append(i)
        self.player.neighbors_opinion_guess_set_include_disconnect = ', '.join(map(str, self.participant.vars['neighbors_opinion_guess_set']))
        self.participant.vars['neighbors_id_set'] = [val for n, val in enumerate(self.participant.vars['neighbors_id_set']) if n not in delete_index]
        self.participant.vars['neighbors_opinion_guess_set_disconnect'] =[val for n, val in enumerate(self.participant.vars['neighbors_opinion_guess_set']) if n in delete_index]
        self.participant.vars['neighbors_opinion_guess_set'] = [val for n, val in enumerate(self.participant.vars['neighbors_opinion_guess_set']) if n not in delete_index]
        self.player.neighbors_opinion_guess_set_disconnect = ', '.join(map(str, self.participant.vars['neighbors_opinion_guess_set_disconnect']))
         

        self.participant.vars['neighbors_opinion_set'] = []
        for neighbor in self.participant.vars['neighbors_id_set']:
            self.participant.vars['neighbors_opinion_set'].append(self.participant.vars['others_last_opinions'][self.participant.vars['others_id_in_group'].index(neighbor)])
        self.player.num_neighbors = len(self.participant.vars['neighbors_opinion_set']) #number of neighbors this round
        self.player.neighbors_id_set = ', '.join(map(str, self.participant.vars['neighbors_id_set']))
        self.player.neighbors_opinion_set = ', '.join(map(str, self.participant.vars['neighbors_opinion_set']))

        self.player.update_neighbor_opinion_1 = None
        self.player.update_neighbor_opinion_2 = None
        self.player.update_neighbor_opinion_3 = None
        self.player.update_neighbor_opinion_4 = None
        self.player.update_neighbor_opinion_5 = None
        self.player.update_neighbor_opinion_6 = None
        self.player.update_neighbor_opinion_7 = None
        self.player.update_neighbor_opinion_8 = None


        if self.player.num_neighbors > 0:
            self.player.neighbor_opinion_1 = self.participant.vars['neighbors_opinion_set'][0]
            self.player.update_neighbor_opinion_1 = self.participant.vars['neighbors_opinion_guess_set'][0]
        if self.player.num_neighbors > 1:
            self.player.neighbor_opinion_2 = self.participant.vars['neighbors_opinion_set'][1]
            self.player.update_neighbor_opinion_2 = self.participant.vars['neighbors_opinion_guess_set'][1]
        if self.player.num_neighbors > 2:
            self.player.neighbor_opinion_3 = self.participant.vars['neighbors_opinion_set'][2]
            self.player.update_neighbor_opinion_3 = self.participant.vars['neighbors_opinion_guess_set'][2]
        if self.player.num_neighbors > 3:
            self.player.neighbor_opinion_4 = self.participant.vars['neighbors_opinion_set'][3]
            self.player.update_neighbor_opinion_4 = self.participant.vars['neighbors_opinion_guess_set'][3]
        if self.player.num_neighbors > 4:
            self.player.neighbor_opinion_5 = self.participant.vars['neighbors_opinion_set'][4]
            self.player.update_neighbor_opinion_5 = self.participant.vars['neighbors_opinion_guess_set'][4]
        if self.player.num_neighbors > 5:
            self.player.neighbor_opinion_6 = self.participant.vars['neighbors_opinion_set'][5]
            self.player.update_neighbor_opinion_6 = self.participant.vars['neighbors_opinion_guess_set'][5]
        if self.player.num_neighbors > 6:
            self.player.neighbor_opinion_7 = self.participant.vars['neighbors_opinion_set'][6]
            self.player.update_neighbor_opinion_7 = self.participant.vars['neighbors_opinion_guess_set'][6]
        if self.player.num_neighbors > 7:
            self.player.neighbor_opinion_8 = self.participant.vars['neighbors_opinion_set'][7]
            self.player.update_neighbor_opinion_8 = self.participant.vars['neighbors_opinion_guess_set'][7]
        self.player.neighbors_opinion_guess_set = ', '.join(map(str, self.participant.vars['neighbors_opinion_guess_set']))
        # self.participant.vars['neighbors_opinion_set'].sort() #reorder neighbors' opinons from low to high
        if (self.player.if_connect_player1 is None) | (self.player.if_connect_player2 is None):
            self.player.if_miss_neighbor = 1
            self.player.payoff = 0

        if self.timeout_happened:
            self.player.timeout_choose_neighbors = 1
        #payoff is what they see in the slider, model_payoff use previous neighbor opinion in calculation
        self.player.model_payoff_round = 0
        if (self.player.num_neighbors == 0) & (self.player.opinion_this_round >= 0):
            self.player.payoff = -(self.player.opinion_this_round-self.player.opinion_last_round)*(self.player.opinion_this_round-self.player.opinion_last_round)
            self.player.model_payoff_round = -(self.player.opinion_this_round - self.player.opinion_last_round) * (self.player.opinion_this_round - self.player.opinion_last_round)
        elif (self.player.num_neighbors > 0) & (self.player.opinion_this_round >= 0) & (any(x is None for x in self.participant.vars['neighbors_opinion_guess_set']) == False):
            for neighbor_Opinion in self.participant.vars['neighbors_opinion_guess_set']:
                self.player.payoff += (Constants.V-Constants.f*(self.player.opinion_this_round - neighbor_Opinion)*(self.player.opinion_this_round - neighbor_Opinion) - (1-Constants.f)*(self.player.opinion_this_round - self.player.opinion_last_round)*(self.player.opinion_this_round - self.player.opinion_last_round))
            for neighbor_Opinion in self.participant.vars['neighbors_opinion_set']:
                self.player.model_payoff_round = self.player.model_payoff_round + (
                    Constants.V - Constants.f * (self.player.opinion_this_round - neighbor_Opinion) * (
                    self.player.opinion_this_round - neighbor_Opinion) - (1 - Constants.f) * (
                            self.player.opinion_this_round - self.player.opinion_last_round) * (
                            self.player.opinion_this_round - self.player.opinion_last_round))
        elif (self.player.num_neighbors > 0) & (self.player.opinion_this_round >= 0):
            for neighbor_Opinion in self.participant.vars['neighbors_opinion_set']:
                self.player.model_payoff_round = self.player.model_payoff_round + (
                            Constants.V - Constants.f * (self.player.opinion_this_round - neighbor_Opinion) * (
                                self.player.opinion_this_round - neighbor_Opinion) - (1 - Constants.f) * (
                                        self.player.opinion_this_round - self.player.opinion_last_round) * (
                                        self.player.opinion_this_round - self.player.opinion_last_round))
        else:
            self.player.payoff = 0

        # If a subject didn't update opinion this round, use previous opinion instead.
        if self.timeout_happened:
            self.player.timeout_update_opinion = 1

        if self.player.opinion_this_round < 0:
            self.player.if_miss_opinion = 1
            self.player.opinion_this_round = self.player.opinion_last_round

        # self.participant.vars['game_payoff'] += self.player.payoff
        # self.player.game_payoff = self.participant.vars['game_payoff']



class BeforeResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'update_neighbor_actual_opinion_eachround'


class Results(Page):

    timeout_seconds = 15

    def vars_for_template(self):
        return {
            'player_all_rounds': self.player.in_all_rounds(),
        }



class GamePayment(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        last_rounds = 5
        game_payoff_selection_list = self.participant.vars['payoff_in_all_rounds'][-last_rounds:]
        self.participant.vars['game_payoff'] = max(random.choice(game_payoff_selection_list), 400) #set lower bound 150
        self.player.game_payoff = round(self.participant.vars['game_payoff'])
        return{
            'game_payoff': round(self.participant.vars['game_payoff']),
        }


class ExperimentPayment(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def vars_for_template(self):
        return {
            'payoff_experiment': round(self.participant.vars['game_payoff']),
            'payoff_experiment_dollar': round(math.sqrt(round(self.participant.vars['game_payoff'])/4),2),
            'total_endowments': Constants.endowment,
            'total_payoff_experiment_dollar': round(round(math.sqrt(round(self.participant.vars['game_payoff'])/4),2) 
            + Constants.participation_fee + Constants.endowment, 2),
        }

    def before_next_page(self):
        self.player.total_payoff_experiment_dollar = round(round(math.sqrt(round(self.participant.vars['game_payoff'])/4),2) +Constants.participation_fee+Constants.endowment,2)


page_sequence = [
    GameInstruction,
    GenerateInitialOpinionWaitPage,
    OpinionUpdateWaitPage,
    GenerateObservedPlayersWaitPage,
    NeighborUpdate,
    BeforeResultsWaitPage,
    Results,
    GamePayment,
    ExperimentPayment,
]