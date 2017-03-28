# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0011_auto_20170307_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselplugin',
            name='interval',
            field=models.IntegerField(default=2000, help_text='interval between slides in milliseconds'),
        ),
    ]
