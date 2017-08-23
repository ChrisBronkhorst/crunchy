from django.db import models


# Create your models here.
# 5 models: Person, Company, Investor, Sector, FundingRound, InvestorFundingContribution

class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    sector = models.ForeignKey(to='Sector', related_name='companies')

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Investor(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class FundingRound(models.Model):
    description = models.TextField()
    company = models.ForeignKey(to=Company, related_name='funding_rounds')
    investors = models.ManyToManyField(to=Investor, through='InvestorFundingRoundContribution',
                                       related_name='funding_rounds')

    def __str__(self):
        return self.description

    @property
    def size(self):
        return sum([contribution.amount for contribution in self.contributions])


class InvestorFundingRoundContribution(models.Model):
    investor = models.ForeignKey(to=Investor, related_name='investments')
    round = models.ForeignKey(to=FundingRound, related_name='contributions')
    amount = models.FloatField()

    def __str__(self):
        return "contribution of: %s" % self.amount






