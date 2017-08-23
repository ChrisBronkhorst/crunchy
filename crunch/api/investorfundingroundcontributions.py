from rest_framework import serializers, permissions, viewsets
from ..models import InvestorFundingRoundContribution


class InvestorFundingRoundContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorFundingRoundContribution
        fields = ['id', 'amount']


class InvestorFundingRoundContributionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = InvestorFundingRoundContributionSerializer
    queryset = InvestorFundingRoundContribution.objects.all()
