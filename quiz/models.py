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
        What is your optimal choice of position if you don’t have neighbors in the current round?
        ''',  # q4
        """Suppose you are in a game ( \( \color{red} V = 150, f = 0.3 \) ). Consider the following situation:  
        In Round 4, your position was \( \color{blue} 30 \).
        In Round 4, you had only one neighbor, and her position was \( \color{blue} 40 \). 
        In Round 5 (current round), you decide not to get any new connections, and change your position to \( \color{blue} 50 \). 
        What is your payoff for Round 5? 
        """,  # q5
        '''
        Suppose you are in a game ( \( \color{red} V = 150, f = 0.3 \) ). Consider the following situation: 
        In Round 7, your position was \( \color{blue} 30 \). 
        In Round 7, you had only one neighbor, and her position was \( \color{blue} 40 \).
        In Round 8 (current round), you decide to connect to an observed player and her position in Round 7 was \( \color{blue} 50 \).
        In Round 8 (current round), you then keep your position to be \( \color{blue} 30 \).
        What is your payoff for Round 8?
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
        [[1, 'A. Increase your position'], [2, 'B. Decrease your position'], [3, 'C. Keep the position the same as the previous round']],  # q4
        [[1, 'A. \( 150 - 0.3 * (50 - 40)^2 - 0.7 * (50 - 30)^2 \)'], [2, 'B. \( 150 - 0.3 * (30 - 40)^2 - 0.7 * (30 - 50)^2 \)']],  # q5
        [[1, 'A. \(  [150 - 0.3 * (40 - 50)^2 - 0.7 * (40 - 40)^2]+[150 - 0.5 * (30 - 30)^2 - 0.5 * (30 - 40)^2] \)'],
         [2, 'B. \(  [150 - 0.3 * (30 - 40)^2 - 0.7 * (30 - 30)^2]+[150 - 0.5 * (30 - 50)^2 - 0.5 * (30 - 30)^2] \)']],  # q6
    ]

    correct_answers = [2, 1, 3, 3, 1, 2]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField(widget=widgets.RadioSelect())
