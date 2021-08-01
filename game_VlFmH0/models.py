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
    name_in_url = 'game_VlFmH0'
    players_per_group = None
    num_rounds = 10
    min_opinion = 0.
    V = 100
    f = 0.5
    h = 0


class Subsession(BaseSubsession):
    def generate_initial_opinion(self):
        initial_opinion_set = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
        random.shuffle(initial_opinion_set)
        for p in self.get_players():
            # p.initial_opinion = round(random.uniform(Constants.min_opinion, 1),
            #                           2)  # generate a random 2-decimal number as the initial opinion
            p.initial_opinion = initial_opinion_set[p.id_in_group - 1] # randomly pick one as initial opinion from initial opinion set
            p.opinion_last_round = p.initial_opinion

    def update_opinion_eachround(self):
        for p in self.get_players():
            p.opinion_last_round = p.in_round(p.round_number - 1).opinion_this_round

    def generate_observed_players_eachround(self):
        for p in self.get_players():
            p.participant.vars['others_last_opinions'] = []
            p.participant.vars['others_id_in_group'] = []
            for other in p.get_others_in_subsession():
                p.participant.vars['others_id_in_group'].append(other.id_in_group) #stores all 10 other players' ids
                p.participant.vars['others_last_opinions'].append(other.opinion_last_round) #stores all 10 other players' last round opinions
            observed_players_id_this_round = random.sample(p.participant.vars['others_id_in_group'], 2) #randomly choose 2 observed players (id)
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
    initial_opinion = models.FloatField(min=Constants.min_opinion, max=1) # The initial opinion assigned to each player
    opinion_last_round = models.FloatField()
    opinion_this_round = models.FloatField(
        null=True, blank=True,
        )
    observed_opinion_player1 = models.FloatField(min=Constants.min_opinion, max=1) # The observed player 1's last round opinion
    observed_opinion_player2 = models.FloatField(min=Constants.min_opinion, max=1) # The observed player 2's last round opinion
    observed_id_player1 = models.IntegerField(min=1, max=11) # The observed player 1's ID
    observed_id_player2 = models.IntegerField(min=1, max=11) # The observed player 2's ID
    if_connect_player1 = models.BooleanField(
        null=True, blank=True,
        widget = widgets.RadioSelectHorizontal(),
        label='Do you want to connect with Player 1?'
    ) # Whether to connect with player 1
    if_connect_player2 = models.BooleanField(
        null=True, blank=True,
        widget = widgets.RadioSelectHorizontal(),
        label='Do you want to connect with Player 2?'
    ) # Whether to connect with player 2
    num_neighbors = models.IntegerField(initial=0)
    disconnect_with_player1 = models.BooleanField()
    disconnect_with_player2 = models.BooleanField()
    if_miss_neighbor = models.BooleanField(initial=0)
    if_miss_opinion = models.BooleanField(initial=0)

    game_payoff = models.CurrencyField()

    timeout_choose_neighbors = models.BooleanField(initial=0)
    timeout_update_opinion = models.BooleanField(initial=0)

    neighbors_id_set = models.LongStringField()
    neighbors_opinion_set = models.LongStringField()

    # def live_getselectedneighbor(self, data):
    #     print(data)
    #     if "player1" in data:
    #         print('connected with player 1')
    #     if "player2" in data:
    #         print('connected with player 2')
    #     print('end of live data send')
