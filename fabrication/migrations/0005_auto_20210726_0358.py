# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-26 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
        ('fabrication', '0004_auto_20210726_0331'),
    ]

    operations = [
        migrations.CreateModel(
            name='FabricationMaterialPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='fabricationcategory',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Placeholder image.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
    ]
