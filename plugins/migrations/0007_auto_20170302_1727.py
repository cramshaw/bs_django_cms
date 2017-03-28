# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('plugins', '0006_auto_20170302_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='HRPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='cms.CMSPlugin', related_name='plugins_hrplugin', serialize=False)),
                ('css_class', models.CharField(choices=[('thick', 'Dark and thick'), ('dark', 'Dark and thin'), ('light', 'Light')], max_length=5, default='light')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='columnplugin',
            name='size',
            field=models.CharField(help_text='The larger the column, the more likely it will stack as screen size decreases.', choices=[('', 'Extra Small'), ('sm-', 'Small'), ('md-', 'Medium'), ('lg-', 'Large'), ('xl-', 'Extra Large')], max_length=3, default='md-'),
        ),
        migrations.AlterField(
            model_name='columnplugin',
            name='width',
            field=models.IntegerField(help_text='This creates a Bootstrap Column, full width is 12.'),
        ),
        migrations.AlterField(
            model_name='mapplugin',
            name='direct_link',
            field=models.URLField(help_text="Generate this by going to Google Maps and pressing 'Share'", null=True),
        ),
    ]
