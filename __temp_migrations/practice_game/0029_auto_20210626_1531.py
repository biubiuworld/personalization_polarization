# Generated by Django 2.2.12 on 2021-06-26 22:31

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_game', '0028_auto_20210625_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='if_connect_player1',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Do you want to connect with Player 1?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='if_connect_player2',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Do you want to connect with Player 2?'),
        ),
    ]
