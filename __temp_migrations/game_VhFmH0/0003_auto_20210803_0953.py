# Generated by Django 2.2.12 on 2021-08-03 16:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('game_VhFmH0', '0002_auto_20210719_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='neighbors_id_set',
            field=otree.db.models.LongStringField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='neighbors_opinion_set',
            field=otree.db.models.LongStringField(null=True),
        ),
    ]
