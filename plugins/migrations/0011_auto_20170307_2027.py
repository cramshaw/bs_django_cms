# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('plugins', '0010_workextension'),
    ]

    operations = [
        migrations.AddField(
            model_name='workextension',
            name='disciplines',
            field=models.ManyToManyField(to='categories.Discipline'),
        ),
        migrations.AddField(
            model_name='workextension',
            name='industries',
            field=models.ManyToManyField(to='categories.Industry'),
        ),
    ]
