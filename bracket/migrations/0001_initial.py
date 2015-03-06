# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=50, null=True, blank=True)),
                ('mascot_name', models.CharField(max_length=25, null=True, blank=True)),
                ('experience_ranking', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('bracket_seed', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('offensive_rebound_ranking', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('steals_ranking', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('away_games_ranking', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
