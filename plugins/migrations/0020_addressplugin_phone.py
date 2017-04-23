# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0019_mapplugin_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressplugin',
            name='phone',
            field=models.TextField(default='+44 (0)20 7833 6494'),
            preserve_default=False,
        ),
    ]
