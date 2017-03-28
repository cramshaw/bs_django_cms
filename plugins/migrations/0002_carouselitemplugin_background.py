# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('plugins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselitemplugin',
            name='background',
            field=filer.fields.image.FilerImageField(null=True, related_name='background', to='filer.Image'),
        ),
    ]
