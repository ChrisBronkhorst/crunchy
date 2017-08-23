# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FundingRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funding_rounds', to='crunch.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorFundingRoundContribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='crunch.Investor')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='crunch.FundingRound')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='fundinground',
            name='investors',
            field=models.ManyToManyField(related_name='funding_rounds', through='crunch.InvestorFundingRoundContribution', to='crunch.Investor'),
        ),
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='crunch.Sector'),
        ),
    ]
