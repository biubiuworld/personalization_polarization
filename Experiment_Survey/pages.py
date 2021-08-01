from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):
    form_model = 'player'
    form_fields = ['First_name', 'Last_name', 'Email', 'Student_ID', 'Session_date', 'Participant_ID', 'Venmo_ID', 'Comments', 'Strategy']



class Results(Page):
    pass


page_sequence = [Survey, Results]
