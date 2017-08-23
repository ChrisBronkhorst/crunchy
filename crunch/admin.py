from django.contrib import admin
from .models import Company, Sector, Investor, FundingRound, InvestorFundingRoundContribution
# Register your models here.

admin.site.register(Company)
admin.site.register(Sector)
admin.site.register(Investor)
admin.site.register(FundingRound)
admin.site.register(InvestorFundingRoundContribution)
