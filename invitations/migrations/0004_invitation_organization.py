# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_auto_20210531_0917'),
        ('invitations', '0003_auto_20151126_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.Organization'),
            preserve_default=False,
        ),

    ]
