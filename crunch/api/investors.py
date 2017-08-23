from rest_framework import serializers, permissions, viewsets
from ..models import Investor
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ['url', 'id', 'name']


class InvestorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (AdminRenderer, BrowsableAPIRenderer, JSONRenderer)
    serializer_class = InvestorSerializer
    queryset = Investor.objects.all()
