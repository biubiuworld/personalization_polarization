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
    num_rounds = 3 #number of quiz questions
    quiz_question_text = [
        '''
        If you don’t have any neighbor, your maximum payoff would be:
        ''', #q1
        '''
        Which of the following statements is true?
        ''', #q2
        '''
        Which of the following statements is not true?
        ''',  # q3
     ]
    quiz_question_choices = [
        [[1, 'A. Any positive number'], [2, 'B. Any negative number'], [3, 'C. 0']],  # q1
        [[1, 'A. If I didn’t select neighbors/update my opinion this round, I would earn 0.'],
         [2, 'B. If I didn’t select neighbors/update my opinion this round, I would earn a random positive payoff.'],
         [3, 'C. If I didn’t select neighbors/update my opinion this round, I would earn a random negative payoff.']],  # q2
        [[1, 'A. Any positive number'], [2, 'B. Any negative number'], [3, 'C. 0']],  # q3

    ]

    correct_answers = [3, 1, 3]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField(widget=widgets.RadioSelect())
