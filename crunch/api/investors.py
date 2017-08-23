from rest_framework import serializers, permissions, viewsets
from ..models import Investor


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ['id', 'name']


class InvestorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = InvestorSerializer
    queryset = Investor.objects.all()
