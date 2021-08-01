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
    name_in_url = 'quiz'
    players_per_group = None
    num_rounds = 6 #number of quiz questions
    quiz_question_text = [
        '''
        Which of the following statements is true?
        ''',  # q1
        '''
        Which of the following statements is true?
        ''', #q2
        '''
        Which of the following statements is true?
        ''',  # q3
        '''
        If you don’t have any neighbor, your maximum payoff would be:
        ''',  # q4
        '''
        Suppose you are in a game ( \( \color{red} V = 150, f = 0.3 \) ). 
        If you have only one neighbor at the beginning of the current round (round 5) and her position in round 4 is \( \color{blue} 50 \). 
        Your own position in round 4 is \( \color{blue} 40 \). If you decide not to connect to anyone and change your position to \( \color{blue} 50 \), 
        then your payoff for this round is___
        ''',  # q5
        '''
        Suppose you are in a game ( \( \color{red} V = 150, f = 0.3 \) ). 
        If you only have one neighbor at the beginning of the current round (round 5) and her opinion in round 4 is \( \color{blue} 50 \). 
        Your own opinion in round 4 is \( \color{blue} 40 \). If you decide to connect to an observed agent whose opinion in round 4 is \( \color{blue} 40 \), 
        and still choose your own opinion to be \( \color{blue} 40 \), then your payoff for this round is___
        ''',  # q6
     ]
    quiz_question_choices = [
        [[1, 'A. The initial position could be 24.'], [2, 'B. The initial position is randomly selected from [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]'], [3, 'C. The initial position could be any number between 0 and 100.']],  # q1
        [[1, 'A. If I didn’t answer neighbor choosing questions, my payoff would be 0 this round.'],
         [2, 'B. If I didn’t answer neighbor choosing questions, my payoff would be a random positive value this round.'],
         [3, 'C. If I didn’t answer neighbor choosing questions, my payoff would be a random negative value this round.']],  # q2
        [[1, 'A. If I didn’t move slider to update my position, my payoff would be a random negative value this round.'],
         [2, 'B. If I didn’t move slider to update my position, my payoff would be a random positive value this round.'],
         [3, 'C. If I didn’t move slider to update my position, my payoff would be 0 this round.']],  # q3
        [[1, 'A. Any positive number'], [2, 'B. Any negative number'], [3, 'C. 0']],  # q4
        [[1, 'A. \( 150 - 0.3 * (50 - 50)^2 - 0.7 * (50 - 40)^2 \)'], [2, 'B. \( 150 - 0.3 * (40 - 50)^2 - 0.7 * (40 - 40)^2 \)']],  # q5
        [[1, 'A. \(  [150 - 0.3 * (40 - 50)^2 - 0.7 * (40 - 40)^2]+[150 - 0.5 * (30 - 30)^2 - 0.5 * (30 - 40)^2] \)'],
         [2, 'B. \(  [150 - 0.3 * (50 - 50)^2 - 0.7 * (50 - 40)^2]+[150 - 0.5 * (50 - 30)^2 - 0.5 * (50 - 40)^2] \)']],  # q6
    ]

    correct_answers = [2, 1, 3, 3, 1, 2]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField(widget=widgets.RadioSelect())
