from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class QuizInstruction(Page):
    def is_displayed(self):
        return self.round_number == 1


class QuizPage(Page):
    form_model = 'player'
    form_fields = ['answer']

    def answer_choices(self):
        return Constants.quiz_question_choices[self.round_number - 1]

    def is_displayed(self):
        return True

    def vars_for_template(self):
        return {
            'questiontext': Constants.quiz_question_text[self.round_number - 1]
        }

    def error_message(self, values):
        if Constants.correct_answers[self.round_number - 1] != values['answer']:
            return "Your answer is not correct. Please select it again."



class Results(Page):
    pass


page_sequence = [QuizInstruction, QuizPage, Results]
