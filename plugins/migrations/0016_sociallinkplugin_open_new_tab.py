# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0015_remove_carouselitemplugin_carousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallinkplugin',
            name='open_new_tab',
            field=models.BooleanField(default=True),
        ),
    ]
