# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('plugins', '0005_auto_20170302_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='RowPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, to='cms.CMSPlugin', related_name='plugins_rowplugin', parent_link=True, auto_created=True, primary_key=True)),
                ('ymargin', models.IntegerField(help_text='on a scale of 1 to 5, as per Bootstrap, adds margin to top and bottom of row')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='mapplugin',
            name='direct_link',
            field=models.URLField(null=True),
        ),
    ]
