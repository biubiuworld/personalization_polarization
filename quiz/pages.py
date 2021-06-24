from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Question1(Page):
    form_model = 'player'
    form_fields = ['question1']

    def error_message(self, values):
        if values['question1'] == 0 or values['question1'] == 1 or values['question1'] == 3:
            return "Your answer is not correct. Player 1 cannot lie, so the true number must be in the message."

    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Question1, ResultsWaitPage, Results]
