from django.db import models


# Create your models here.
# 5 models, Person, Company, Investor, FundingRound, Sector, Employee

class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    sector = models.ForeignKey(to=Sector, related_name='companies')


class Sector(models.Model):
    name = models.CharField(max_length=150)


class Investor(models.Model):
    name = models.CharField(max_length=150)


class FundingRound(models.Model):
    description = models.TextField()
    company = models.ForeignKey(to=Company, related_name='funding_rounds')
    investors = models.ManyToManyField(to=Investor, through='InvestorFundingRoundContribution',
                                       related_name='funding_rounds')


class InvestorFundingRoundContribution(models.Model):
    investor = models.ForeignKey(to=Investor, related_name='investments')
    round = models.ForeignKey(to=FundingRound, related_name='contributions')
    amount = models.FloatField()





