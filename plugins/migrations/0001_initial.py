# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItemPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, related_name='plugins_carouselitemplugin', primary_key=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CarouselPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, related_name='plugins_carouselplugin', primary_key=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='carouselitemplugin',
            name='carousel',
            field=models.ForeignKey(related_name='slides', to='plugins.CarouselPlugin'),
        ),
    ]
