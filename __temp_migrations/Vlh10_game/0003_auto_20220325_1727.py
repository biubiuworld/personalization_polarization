# Generated by Django 2.2.12 on 2022-03-26 00:27

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Vlh10_game', '0002_player_exchange_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='neighbors_id_set_after_choose_neighbors',
            field=otree.db.models.LongStringField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='neighbors_opinion_guess_set_disconnect',
            field=otree.db.models.LongStringField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='neighbors_opinion_guess_set_include_disconnect',
            field=otree.db.models.LongStringField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='neighbors_opinion_set_after_choose_neighbors',
            field=otree.db.models.LongStringField(null=True),
        ),
    ]