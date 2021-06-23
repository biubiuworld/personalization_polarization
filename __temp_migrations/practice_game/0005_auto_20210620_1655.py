# Generated by Django 2.2.12 on 2021-06-20 23:55

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_game', '0004_auto_20210617_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='observed_player1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='observed_player2',
        ),
        migrations.AddField(
            model_name='player',
            name='observed_id_player1',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='observed_id_player2',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='observed_opinion_player1',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='observed_opinion_player2',
            field=otree.db.models.FloatField(null=True),
        ),
    ]
