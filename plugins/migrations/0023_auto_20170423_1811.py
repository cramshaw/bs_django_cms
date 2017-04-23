# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0022_socialshareplugin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallinkplugin',
            name='icon',
        ),
        migrations.AddField(
            model_name='sociallinkplugin',
            name='icon_class',
            field=models.CharField(default='fa fa-twitter', max_length=20),
        ),
    ]
