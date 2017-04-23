# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('plugins', '0021_auto_20170423_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialSharePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, to='cms.CMSPlugin', auto_created=True, parent_link=True, primary_key=True, related_name='plugins_socialshareplugin')),
                ('share_to_pinterest', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
