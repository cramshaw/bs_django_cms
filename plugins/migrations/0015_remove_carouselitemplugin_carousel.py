# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0014_auto_20170401_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouselitemplugin',
            name='carousel',
        ),
    ]
