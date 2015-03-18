# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0002_ranking_strenghth_of_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ranking',
            old_name='strenghth_of_schedule',
            new_name='strength_of_schedule',
        ),
    ]
