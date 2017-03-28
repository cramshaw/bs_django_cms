# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('plugins', '0004_auto_20170302_1604'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SocialLinksBlockPlugin',
        ),
    ]
