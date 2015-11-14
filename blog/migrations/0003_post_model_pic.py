# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='model_pic',
            field=models.ImageField(default='blog/static/images/None/no-img.jpg', upload_to='blog/static/images/'),
        ),
    ]
