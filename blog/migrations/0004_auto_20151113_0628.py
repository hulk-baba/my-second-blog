# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_model_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='model_pic',
            field=models.ImageField(default='blog/static/images/already.png', upload_to='blog/static/images/'),
        ),
    ]
