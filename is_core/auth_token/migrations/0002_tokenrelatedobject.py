# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth_token', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenRelatedObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.TextField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('token', models.ForeignKey(related_name='related_objects', to='auth_token.Token')),
            ],
        ),
    ]
