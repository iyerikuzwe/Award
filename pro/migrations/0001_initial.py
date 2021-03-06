# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 08:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DesignRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_pic', models.ImageField(blank=True, upload_to='images/')),
                ('bio', models.TextField()),
                ('contact', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('landing_page', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=100)),
                ('rating', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsabilityRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Project')),
            ],
        ),
        migrations.AddField(
            model_name='designrating',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Profile'),
        ),
        migrations.AddField(
            model_name='designrating',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Project'),
        ),
        migrations.AddField(
            model_name='contentrating',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Profile'),
        ),
        migrations.AddField(
            model_name='contentrating',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Project'),
        ),
    ]
