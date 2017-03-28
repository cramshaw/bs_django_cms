# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
        ('plugins', '0008_linkedsectionplugin_linkvideoplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, to='cms.CMSPlugin', related_name='plugins_awardplugin', parent_link=True, auto_created=True)),
                ('text', models.TextField()),
                ('logo', filer.fields.image.FilerImageField(null=True, to='filer.Image', related_name='award_logo')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
