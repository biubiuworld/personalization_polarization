# Generated by Django 2.2.12 on 2021-07-31 18:36

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment_payment_dollar', '0002_auto_20210719_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='Comments',
            field=otree.db.models.LongStringField(null=True, verbose_name='Is there any part of the experiment that makes your confusing? Please give us some comments.'),
        ),
        migrations.AddField(
            model_name='player',
            name='Email',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='Your UCSC email'),
        ),
        migrations.AddField(
            model_name='player',
            name='First_name',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='Your First Name'),
        ),
        migrations.AddField(
            model_name='player',
            name='Last_name',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='Your Last Name'),
        ),
        migrations.AddField(
            model_name='player',
            name='Participant_ID',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='Your participant ID (The participant ID is the user name in the Zoom chat room (e.g. leeps_x where x is a number). If you are not assigned and ID, fill in "show-up")'),
        ),
        migrations.AddField(
            model_name='player',
            name='Session_date',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='The session date you are attending (mm/dd/yyyy)'),
        ),
        migrations.AddField(
            model_name='player',
            name='Strategy',
            field=otree.db.models.LongStringField(null=True, verbose_name='How do you play this game? Please describe your strategy based on your role and the rules.'),
        ),
        migrations.AddField(
            model_name='player',
            name='Student_ID',
            field=otree.db.models.IntegerField(null=True, verbose_name='Your UCSC student ID'),
        ),
        migrations.AddField(
            model_name='player',
            name='Venmo_ID',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='Your Venmo account ID (We will pay you in 48 hours after the session ends.)'),
        ),
    ]
