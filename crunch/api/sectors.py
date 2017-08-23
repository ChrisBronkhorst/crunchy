from rest_framework import serializers, permissions, viewsets
from ..models import Sector


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id', 'name']


class SectorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
