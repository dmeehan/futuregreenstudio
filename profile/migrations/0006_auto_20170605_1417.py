# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('profile', '0005_auto_20170510_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('job_title', models.CharField(max_length=255)),
                ('bio', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='employee',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profilepageemployee',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='profilepageemployee',
            name='page',
        ),
        migrations.AlterField(
            model_name='profilepageclient',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='design.Client'),
        ),
        migrations.AlterField(
            model_name='profilepageclient',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='profile.ProfilePage'),
        ),
        migrations.AlterField(
            model_name='profilepagecollaborator',
            name='collaborator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='design.Collaborator'),
        ),
        migrations.AlterField(
            model_name='profilepagecollaborator',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='collaborators', to='profile.ProfilePage'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Collaborator',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='ProfilePageEmployee',
        ),
    ]