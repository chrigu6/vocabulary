# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 19:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asked', models.IntegerField(default=0)),
                ('correct', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(default=b'', max_length=200, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=200)),
                ('date_created', models.DateField(auto_now=True)),
                ('cards', models.ManyToManyField(to='trainer.Card')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Set',
                'verbose_name_plural': 'Sets',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(default=b'', max_length=200)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.Language')),
            ],
            options={
                'verbose_name': 'Word',
                'verbose_name_plural': 'Words',
            },
        ),
        migrations.AddField(
            model_name='card',
            name='first_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_language', to='trainer.Language'),
        ),
        migrations.AddField(
            model_name='card',
            name='first_language_word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.Word'),
        ),
        migrations.AddField(
            model_name='card',
            name='second_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_language', to='trainer.Language'),
        ),
        migrations.AddField(
            model_name='card',
            name='second_language_words',
            field=models.ManyToManyField(related_name='second_language', to='trainer.Word'),
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together=set([('word', 'language')]),
        ),
    ]
