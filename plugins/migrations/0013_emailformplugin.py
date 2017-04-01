# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('plugins', '0012_carouselplugin_interval'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailFormPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, to='cms.CMSPlugin', related_name='plugins_emailformplugin', auto_created=True, primary_key=True)),
                ('css_class', models.CharField(default='light', choices=[('dark', 'Black'), ('light', 'White')], max_length=5)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
