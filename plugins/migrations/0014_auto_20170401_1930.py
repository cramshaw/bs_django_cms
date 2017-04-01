# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0013_emailformplugin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailformplugin',
            name='css_class',
            field=models.CharField(max_length=5, choices=[('black', 'Black'), ('white', 'White')], default='light'),
        ),
    ]
