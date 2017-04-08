# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0016_sociallinkplugin_open_new_tab'),
    ]

    operations = [
        migrations.AddField(
            model_name='rowplugin',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
