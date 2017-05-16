# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0023_auto_20170423_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='workextension',
            name='allow_access',
            field=models.BooleanField(default=True),
        ),
    ]
