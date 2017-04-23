# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0020_addressplugin_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplugin',
            name='height',
            field=models.CharField(max_length=10, default='500px'),
        ),
    ]
