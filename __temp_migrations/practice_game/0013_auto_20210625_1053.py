# Generated by Django 2.2.12 on 2021-06-25 17:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_game', '0012_auto_20210625_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='opinion_this_round',
            field=otree.db.models.FloatField(null=True, verbose_name='Please update your opinion in this round'),
        ),
    ]
