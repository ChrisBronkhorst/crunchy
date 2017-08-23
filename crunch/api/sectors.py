from rest_framework import serializers, permissions, viewsets
from ..models import Sector
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['url', 'id', 'name']


class SectorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (AdminRenderer, BrowsableAPIRenderer, JSONRenderer)
    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
