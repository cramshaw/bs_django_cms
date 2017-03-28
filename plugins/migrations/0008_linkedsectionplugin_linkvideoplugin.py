# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('cms', '0016_auto_20160608_1535'),
        ('plugins', '0007_auto_20170302_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedSectionPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', related_name='plugins_linkedsectionplugin', auto_created=True, parent_link=True, serialize=False, primary_key=True)),
                ('index', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='LinkVideoPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', related_name='plugins_linkvideoplugin', auto_created=True, parent_link=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=25)),
                ('jump_to_index', models.CharField(max_length=10)),
                ('video', filer.fields.file.FilerFileField(related_name='link_video', to='filer.File')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
