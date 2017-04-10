# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0017_rowplugin_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressplugin',
            name='direct_link',
            field=models.URLField(help_text="Generate this by going to Google Maps and pressing 'Share'", null=True),
        ),
    ]
