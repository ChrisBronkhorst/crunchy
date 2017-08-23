from rest_framework import serializers, permissions, viewsets
from ..models import FundingRound
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer

class FundingRoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingRound
        fields = ['url', 'id', 'description', 'size', 'company']


class FundingRoundViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (AdminRenderer, BrowsableAPIRenderer, JSONRenderer)
    serializer_class = FundingRoundSerializer
    queryset = FundingRound.objects.all()
