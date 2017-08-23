from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers
from crunch.api.users import UserViewSet
from crunch.api.companies import CompanyViewSet
from crunch.api.sectors import SectorViewSet
from crunch.api.investors import InvestorViewSet
from crunch.api.fundingrounds import FundingRoundViewSet
from crunch.api.investorfundingroundcontributions import InvestorFundingRoundContributionViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'sectors', SectorViewSet)
router.register(r'investors', InvestorViewSet)
router.register(r'funding-rounds', FundingRoundViewSet)
router.register(r'investor-funding-round-contributions', InvestorFundingRoundContributionViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='crunch/home.html'), name='home'),
    url(r'api/', include(router.urls))
]

