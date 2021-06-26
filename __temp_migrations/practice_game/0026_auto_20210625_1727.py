# Generated by Django 2.2.12 on 2021-06-26 00:27

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_game', '0025_auto_20210625_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='opinion_this_round',
            field=otree.db.models.FloatField(default=float("nan"), help_text='Note: please fill in a number between 0 and 1', null=True, verbose_name='Please update your opinion in this round'),
        ),
    ]
