from rest_framework import serializers, permissions, viewsets
from ..models import FundingRound


class FundingRoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingRound
        fields = ['id', 'description', 'size']


class FundingRoundViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FundingRoundSerializer
    queryset = FundingRound.objects.all()
