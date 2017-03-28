# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
        ('plugins', '0009_awardplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('extended_object', models.OneToOneField(editable=False, to='cms.Page')),
                ('image', filer.fields.image.FilerImageField(related_name='work_display_image', null=True, to='filer.Image')),
                ('public_extension', models.OneToOneField(editable=False, related_name='draft_extension', null=True, to='plugins.WorkExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
