from rest_framework import serializers, permissions, viewsets
from ..models import InvestorFundingRoundContribution
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer

class InvestorFundingRoundContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorFundingRoundContribution
        fields = ['url', 'id', 'amount', 'investor', 'round']


class InvestorFundingRoundContributionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (AdminRenderer, BrowsableAPIRenderer, JSONRenderer)
    serializer_class = InvestorFundingRoundContributionSerializer
    queryset = InvestorFundingRoundContribution.objects.all()
