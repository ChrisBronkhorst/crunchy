from rest_framework import serializers, permissions, viewsets
from ..models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
