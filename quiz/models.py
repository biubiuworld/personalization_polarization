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
    num_rounds = 7 #number of quiz questions
    quiz_question_text = [
        '''
        Which of the following statements is true?
        ''',  # q1
        '''
        Which of the following statements is true?
        ''',  # q2
        '''
        What is your optimal choice of position if you don’t have neighbors in the current round?
        ''',  # q3
        '''
        Which of the following statements is true?
        ''',  # q4
        '''
        Which of the following statements is true?
        ''',  # q5
        """Consider the following situation:  
        In Round 4, your position was \( \color{blue} 30 \).
        In Round 4, you had only one neighbor, and her position was \( \color{blue} 40 \). 
        In Round 5 (current round), you decide not to get any new connections, and change your position to \( \color{blue} 50 \). 
        In Round 5 (current round), your neighbor’s actual position is \( \color{blue} 42 \).
        What is your actual payoff for Round 5? 
        """,  # q6
        '''
        Consider the following situation: 
        In Round 7, your position was \( \color{blue} 30 \). 
        In Round 7, you had only one neighbor A, and her position was \( \color{blue} 40 \).
        In Round 8 (current round), you decide to connect to an observed player B and her position in Round 7 was \( \color{blue} 50 \).
        In Round 8 (current round), you then keep your position to be \( \color{blue} 30 \).
        In Round 8 (current round), your neighbors’ actual positions are \( \color{blue} 42 \) for A and \( \color{blue} 55 \) for B.
        What is your actual payoff for Round 8?
        ''',  # q7
     ]
    quiz_question_choices = [
        [[1, 'A. The initial position could be 24.'], [2, 'B. The initial position is randomly selected from [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0]'], [3, 'C. The initial position could be any number between 0 and 80.']],  # q1
        [[1, 'A. If I didn’t move slider to update my position, my payoff would be a random negative value this round.'],
         [2, 'B. If I didn’t move slider to update my position, my payoff would be a random positive value this round.'],
         [3, 'C. If I didn’t move slider to update my position, my payoff would be 0 this round.']],  # q2
        [[1, 'A. Increase your position'], [2, 'B. Decrease your position'], [3, 'C. Keep the position the same as the previous round']],  # q3
        [[1, 'A. The payoff below the slider is the actual payoff each round.'], [2, 'B. The payoff below the slider is not the actual payoff each round.']],  # q4
        [[1, 'A. The payoff below the slider is calculated based on your position in previous and current round, and the guess of your neighbors’ positions.'],
         [2, 'B. The actual payoff is calculated based on your position in previous and current round, and the guess of your neighbors’ positions.'],
         [3, 'C. The actual payoff is calculated based on your position in previous and current round, and your neighbors’ updated positions.'],
         [4, 'D. Both A and B are correct.'], [5, 'E. Both A and C are correct.']],  # q5
        [[1, 'A. \( 50 - 0.5 * (50 - 40)^2 - 0.5 * (50 - 30)^2 \)'], [2, 'B. \( 50 - 0.5 * (30 - 40)^2 - 0.5 * (30 - 50)^2  \)'],
         [3, 'C. \( 50 - 0.5 * (30 - 42)^2 - 0.5 * (30 - 50)^2 \)'], [4, 'D. \( 50 - 0.5 * (50 - 42)^2 - 0.5 * (50 - 30)^2  \)']],  # q6
        [[1, 'A. \(  [50 - 0.5 * (40 - 50)^2 - 0.5 * (40 - 40)^2]+[50 - 0.5 * (30 - 30)^2 - 0.5 * (30 - 40)^2]  \)'],
         [2, 'B. \(  [50 - 0.5 * (30 - 40)^2 - 0.5 * (30 - 30)^2]+[50 - 0.5 * (30 - 50)^2 - 0.5 * (30 - 30)^2] \)'],
         [3, 'A. \(  [50 - 0.5 * (30 - 42)^2 - 0.5 * (30 - 30)^2]+[50 - 0.5 * (30 - 55)^2 - 0.5 * (30 - 30)^2] \)'],
         [4, 'B. \(  [50 - 0.5 * (30 - 42)^2 - 0.5 * (30 - 30)^2]+[50 - 0.5 * (30 - 50)^2 - 0.5 * (30 - 30)^2] \)']
         ],  # q7
    ]

    correct_answers = [2, 3, 3, 2, 5, 4, 3]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField(widget=widgets.RadioSelect())
