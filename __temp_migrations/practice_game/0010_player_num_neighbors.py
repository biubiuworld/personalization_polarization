# Generated by Django 2.2.12 on 2021-06-22 20:02

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_game', '0009_auto_20210622_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='num_neighbors',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
    ]
