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
import numpy as np

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'game_FmH10'
    players_per_group = None
    num_rounds = 5
    min_opinion = 0.
    V = 250
    f = 0.5
    h = 10
    participation_fee = 4.00
    dollar_per_credit = 0.0025
    endowment = 3.00

class Subsession(BaseSubsession):
    def generate_initial_opinion(self):
        initial_opinion_set = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0]
        random.shuffle(initial_opinion_set)
        for p in self.get_players():
            # p.initial_opinion = round(random.uniform(Constants.min_opinion, 1),
            #                           2)  # generate a random 2-decimal number as the initial opinion
            p.initial_opinion = initial_opinion_set[p.id_in_group - 1] # randomly pick one as initial opinion from initial opinion set
            p.opinion_last_round = p.initial_opinion

    def update_opinion_eachround(self):
        for p in self.get_players():
            p.opinion_last_round = p.in_round(p.round_number - 1).opinion_this_round


    def update_neighbor_actual_opinion_eachround(self):
        for p in self.get_players():
            p.participant.vars['others_update_opinions'] = []
            p.participant.vars['neighbors_actual_opinion_set'] = []
            for other in p.get_others_in_subsession():
                p.participant.vars['others_update_opinions'].append(
                    other.opinion_this_round)  # stores all 8 other players' this round opinions
        for p in self.get_players():
            for neighbor in p.participant.vars['neighbors_id_set']:
                p.participant.vars['neighbors_actual_opinion_set'].append(p.participant.vars['others_update_opinions'][
                                                                          p.participant.vars[
                                                                              'others_id_in_group'].index(neighbor)])
            if len(p.participant.vars['neighbors_actual_opinion_set']) == 1:
                p.actual_opinion_neighbor_1 = p.participant.vars['neighbors_actual_opinion_set'][0]
            if len(p.participant.vars['neighbors_actual_opinion_set']) == 2:
                p.actual_opinion_neighbor_1 = p.participant.vars['neighbors_actual_opinion_set'][0]
                p.actual_opinion_neighbor_2 = p.participant.vars['neighbors_actual_opinion_set'][1]
            if len(p.participant.vars['neighbors_actual_opinion_set']) == 3:
                p.actual_opinion_neighbor_1 = p.participant.vars['neighbors_actual_opinion_set'][0]
                p.actual_opinion_neighbor_2 = p.participant.vars['neighbors_actual_opinion_set'][1]
                p.actual_opinion_neighbor_3 = p.participant.vars['neighbors_actual_opinion_set'][2]
            if len(p.participant.vars['neighbors_actual_opinion_set']) == 4:
                p.actual_opinion_neighbor_1 = p.participant.vars['neighbors_actual_opinion_set'][0]
                p.actual_opinion_neighbor_2 = p.participant.vars['neighbors_actual_opinion_set'][1]
                p.actual_opinion_neighbor_3 = p.participant.vars['neighbors_actual_opinion_set'][2]
                p.actual_opinion_neighbor_4 = p.participant.vars['neighbors_actual_opinion_set'][3]
            if len(p.participant.vars['neighbors_actual_opinion_set']) == 5:
                p.actual_opinion_neighbor_1 = p.participant.vars['neighbors_actual_opinion_set'][0]
                p.actual_opinion_neighbor_2 = p.participant.vars['neighbors_actual_opinion_set'][1]
                p.actual_opinion_neighbor_3 = p.participant.vars['neighbors_actual_opinion_set'][2]
                p.actual_opinion_neighbor_4 = p.participant.vars['neighbors_actual_opinion_set'][3]
                p.actual_opinion_neighbor_5 = p.participant.vars['neighbors_actual_opinion_set'][4]
            if len(p.participant.vars['neighbors_actual_opinion_set']) == 6:
                p.actual_opinion_neighbor_1 = p.participant.vars['neighbors_actual_opinion_set'][0]
                p.actual_opinion_neighbor_2 = p.participant.vars['neighbors_actual_opinion_set'][1]
                p.actual_opinion_neighbor_3 = p.participant.vars['neighbors_actual_opinion_set'][2]
                p.actual_opinion_neighbor_4 = p.participant.vars['neighbors_actual_opinion_set'][3]
                p.actual_opinion_neighbor_5 = p.participant.vars['neighbors_actual_opinion_set'][4]
                p.actual_opinion_neighbor_6 = p.participant.vars['neighbors_actual_opinion_set'][5]
            if len(p.participant.vars['neighbors_actual_opinion_set']) == 7:
                p.actual_opinion_neighbor_1 = p.participant.vars['neighbors_actual_opinion_set'][0]
                p.actual_opinion_neighbor_2 = p.participant.vars['neighbors_actual_opinion_set'][1]
                p.actual_opinion_neighbor_3 = p.participant.vars['neighbors_actual_opinion_set'][2]
                p.actual_opinion_neighbor_4 = p.participant.vars['neighbors_actual_opinion_set'][3]
                p.actual_opinion_neighbor_5 = p.participant.vars['neighbors_actual_opinion_set'][4]
                p.actual_opinion_neighbor_6 = p.participant.vars['neighbors_actual_opinion_set'][5]
                p.actual_opinion_neighbor_7 = p.participant.vars['neighbors_actual_opinion_set'][6]
            if len(p.participant.vars['neighbors_actual_opinion_set']) == 8:
                p.actual_opinion_neighbor_1 = p.participant.vars['neighbors_actual_opinion_set'][0]
                p.actual_opinion_neighbor_2 = p.participant.vars['neighbors_actual_opinion_set'][1]
                p.actual_opinion_neighbor_3 = p.participant.vars['neighbors_actual_opinion_set'][2]
                p.actual_opinion_neighbor_4 = p.participant.vars['neighbors_actual_opinion_set'][3]
                p.actual_opinion_neighbor_5 = p.participant.vars['neighbors_actual_opinion_set'][4]
                p.actual_opinion_neighbor_6 = p.participant.vars['neighbors_actual_opinion_set'][5]
                p.actual_opinion_neighbor_7 = p.participant.vars['neighbors_actual_opinion_set'][6]
                p.actual_opinion_neighbor_8 = p.participant.vars['neighbors_actual_opinion_set'][7]

        for p in self.get_players():
            p.neighbors_actual_opinion_set = ', '.join(map(str, p.participant.vars['neighbors_actual_opinion_set']))
            p.actual_payoff_round = 0
            if p.num_neighbors == 0:
                p.actual_payoff_round = -(p.opinion_this_round - p.opinion_last_round)**2
            elif p.num_neighbors > 0:
                for neighbor_Opinion in p.participant.vars['neighbors_actual_opinion_set']:
                    p.actual_payoff_round = p.actual_payoff_round + Constants.V - Constants.f*(p.opinion_this_round - neighbor_Opinion)**2 - (1 - Constants.f)*(p.opinion_this_round - p.opinion_last_round)**2

    def generate_observed_players_eachround(self):
        for p in self.get_players():
            p.participant.vars['others_last_opinions'] = []
            p.participant.vars['others_id_in_group'] = []
            p.participant.vars['others_p'] = []
            p.participant.vars['total_p'] = 0
            for other in p.get_others_in_subsession():
                p.participant.vars['total_p'] += (1.-0.01*abs(p.opinion_last_round - other.opinion_last_round))**Constants.h
            for other in p.get_others_in_subsession():
                p.participant.vars['others_id_in_group'].append(other.id_in_group) #stores all 10 other players' ids
                p.participant.vars['others_last_opinions'].append(other.opinion_last_round) #stores all 10 other players' last round opinions
                p.participant.vars['others_p'].append(((1.-0.01*abs(p.opinion_last_round - other.opinion_last_round))**Constants.h)/p.participant.vars['total_p'])
            observed_players_id_this_round = np.random.choice(np.asarray(p.participant.vars['others_id_in_group']),
                                                              size=2,
                                                              replace=False,
                                                              p=np.asarray(p.participant.vars['others_p']))

            # observed_players_id_this_round = random.sample(p.participant.vars['others_id_in_group'], 2) #randomly choose 2 observed players (id)
            p.observed_id_player1 = observed_players_id_this_round[0]
            p.observed_id_player2 = observed_players_id_this_round[1]
            p.observed_opinion_player1 = p.participant.vars['others_last_opinions'][p.participant.vars['others_id_in_group'].index(p.observed_id_player1)]
            p.observed_opinion_player2 = p.participant.vars['others_last_opinions'][p.participant.vars['others_id_in_group'].index(p.observed_id_player2)]

            # Whether 2 observed players are already in neighbor set. If so, return whether to disconnect.
            if p.observed_id_player1 in p.participant.vars['neighbors_id_set']:
                p.disconnect_with_player1 = 1
            else:
                p.disconnect_with_player1 = 0

            if p.observed_id_player2 in p.participant.vars['neighbors_id_set']:
                p.disconnect_with_player2 = 1
            else:
                p.disconnect_with_player2 = 0




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    initial_opinion = models.FloatField(min=Constants.min_opinion, max=1)  # The initial opinion assigned to each player
    opinion_last_round = models.FloatField()
    opinion_this_round = models.FloatField(
        null=True, blank=True,
    )
    observed_opinion_player1 = models.FloatField(min=Constants.min_opinion,
                                                 max=1)  # The observed player 1's last round opinion
    observed_opinion_player2 = models.FloatField(min=Constants.min_opinion,
                                                 max=1)  # The observed player 2's last round opinion
    observed_id_player1 = models.IntegerField(min=1, max=11)  # The observed player 1's ID
    observed_id_player2 = models.IntegerField(min=1, max=11)  # The observed player 2's ID
    if_connect_player1 = models.BooleanField(
        null=True,
        widget=widgets.RadioSelectHorizontal(),
        label='Do you want to connect with Player 1?'
    )  # Whether to connect with player 1
    if_connect_player2 = models.BooleanField(
        null=True,
        widget=widgets.RadioSelectHorizontal(),
        label='Do you want to connect with Player 2?'
    )  # Whether to connect with player 2
    num_neighbors = models.IntegerField(initial=0)
    disconnect_with_player1 = models.BooleanField()
    disconnect_with_player2 = models.BooleanField()
    if_miss_neighbor = models.BooleanField(initial=0)
    if_miss_opinion = models.BooleanField(initial=0)

    game_payoff = models.CurrencyField()
    actual_payoff_round = models.CurrencyField()

    timeout_choose_neighbors = models.BooleanField(initial=0)
    timeout_update_opinion = models.BooleanField(initial=0)

    neighbors_id_set = models.LongStringField()
    neighbors_opinion_set = models.LongStringField()

    neighbor_opinion_1 = models.FloatField()
    neighbor_opinion_2 = models.FloatField()
    neighbor_opinion_3 = models.FloatField()
    neighbor_opinion_4 = models.FloatField()
    neighbor_opinion_5 = models.FloatField()
    neighbor_opinion_6 = models.FloatField()
    neighbor_opinion_7 = models.FloatField()
    neighbor_opinion_8 = models.FloatField()

    neighbors_opinion_guess_set = models.LongStringField()
    update_neighbor_opinion_1 = models.IntegerField(label='', min=0, max=80,blank=True)
    update_neighbor_opinion_2 = models.IntegerField(label='', min=0, max=80,blank=True)
    update_neighbor_opinion_3 = models.IntegerField(label='', min=0, max=80,blank=True)
    update_neighbor_opinion_4 = models.IntegerField(label='', min=0, max=80,blank=True)
    update_neighbor_opinion_5 = models.IntegerField(label='', min=0, max=80,blank=True)
    update_neighbor_opinion_6 = models.IntegerField(label='', min=0, max=80,blank=True)
    update_neighbor_opinion_7 = models.IntegerField(label='', min=0, max=80,blank=True)
    update_neighbor_opinion_8 = models.IntegerField(label='', min=0, max=80,blank=True)

    neighbors_actual_opinion_set = models.LongStringField()
    actual_opinion_neighbor_1 = models.FloatField()
    actual_opinion_neighbor_2 = models.FloatField()
    actual_opinion_neighbor_3 = models.FloatField()
    actual_opinion_neighbor_4 = models.FloatField()
    actual_opinion_neighbor_5 = models.FloatField()
    actual_opinion_neighbor_6 = models.FloatField()
    actual_opinion_neighbor_7 = models.FloatField()
    actual_opinion_neighbor_8 = models.FloatField()

    total_payoff_experiment_dollar = models.FloatField()
