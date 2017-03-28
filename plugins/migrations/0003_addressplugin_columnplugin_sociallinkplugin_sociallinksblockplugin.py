# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('cms', '0016_auto_20160608_1535'),
        ('plugins', '0002_carouselitemplugin_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, related_name='plugins_addressplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ColumnPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, related_name='plugins_columnplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('size', models.CharField(choices=[('', 'Extra Small'), ('sm-', 'Small'), ('md-', 'Medium'), ('lg-', 'Large'), ('xl-', 'Extra Large')], max_length=3, default='md-')),
                ('width', models.IntegerField(help_text='This creates a Bootstrap Column, max-width is 12')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SocialLinkPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, related_name='plugins_sociallinkplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('text', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('icon', filer.fields.image.FilerImageField(null=True, related_name='social_icon', to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SocialLinksBlockPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, related_name='plugins_sociallinksblockplugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
