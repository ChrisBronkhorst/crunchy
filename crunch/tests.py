from django.test import TestCase
from .models import Company, Sector, Investor, FundingRound, InvestorFundingRoundContribution
# Create your tests here.



class DataModelUseCaseTests(TestCase):
    def setUp(self):

        # create sectors
        self.soft_drinks = Sector.objects.create(name='soft drinks')
        self.mining = Sector.objects.create(name='mining')

        # create a company
        self.coke = Company.objects.create(name='coke',
                                           description='the company that makes coke',
                                           sector=self.soft_drinks)
        self.virgin = Company.objects.create(name='virgin',
                                           description='the company that makes virgin cola',
                                           sector=self.soft_drinks)
        self.pepsi = Company.objects.create(name='pepsi',
                                           description='the company that makes pepsi',
                                           sector=self.soft_drinks)

        # create investors
        self.scion = Investor.objects.create(name='scion')
        self.alphabet = Investor.objects.create(name='alphabet')

        # create investor funding rounds
        self.coke_series_a = FundingRound.objects.create(description='coke series A funding',
                                                         company=self.coke)
        self.coke_series_b = FundingRound.objects.create(description='coke series B funding',
                                                         company=self.coke)

        # create investor contributions
        self.scion_series_a = InvestorFundingRoundContribution.objects.create(investor=self.scion,
                                                                              round=self.coke_series_a,
                                                                              amount=500000)
        self.alphabet_series_a = InvestorFundingRoundContribution.objects.create(investor=self.alphabet,
                                                                                 round=self.coke_series_a,
                                                                                 amount=1000000)
        self.scion_series_b = InvestorFundingRoundContribution.objects.create(investor=self.scion,
                                                                              round=self.coke_series_b,
                                                                              amount=10000000)



    def test_investment_round(self):
        # how much was coke's series a funding round
        self.assertEqual(self.coke_series_a.size, 1500000)

    def test_total_investments(self):
        # list of investors in coke
        total = sum([funding_round.size for funding_round in FundingRound.objects.filter(company=self.coke)])
        self.assertEqual(total, 11500000)

    def test_investors_in_round(self):
        self.assertEqual(list(self.coke_series_a.investors.all()), [self.scion, self.alphabet])

    def test_companies_in_sector(self):
        self.assertSetEqual(set(self.soft_drinks.companies.all()),
                            set([self.coke, self.pepsi, self.virgin]))