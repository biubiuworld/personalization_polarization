# Generated by Django 2.2.12 on 2021-08-01 00:54

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('game_VhFhH0', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='game_payoff',
            field=otree.db.models.CurrencyField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='timeout_choose_neighbors',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='timeout_update_opinion',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='opinion_this_round',
            field=otree.db.models.FloatField(blank=True, null=True),
        ),
    ]
