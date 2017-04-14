# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0018_addressplugin_direct_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapplugin',
            name='height',
            field=models.CharField(default='500px', max_length='10'),
        ),
    ]
