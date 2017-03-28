# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('plugins', '0003_addressplugin_columnplugin_sociallinkplugin_sociallinksblockplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, to='cms.CMSPlugin', related_name='plugins_mapplugin', primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('zoom', models.IntegerField()),
                ('label', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        )
    ]
