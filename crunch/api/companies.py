from rest_framework import serializers, permissions, viewsets, filters
from ..models import Company, Sector
from .fundingrounds import FundingRoundSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer
from .sectors import SectorSerializer

class CompanySerializer(serializers.ModelSerializer):
    funding_rounds = FundingRoundSerializer(many=True, read_only=True)
    sector_id = serializers.PrimaryKeyRelatedField(source='sector', write_only=True,
                                                   queryset=Sector.objects.all())
    sector = SectorSerializer(read_only=True)
    class Meta:
        model = Company
        fields = ['url', 'id', 'name', 'description', 'funding_rounds', 'sector', 'sector_id']


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CompanySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description',)
    renderer_classes = (AdminRenderer, BrowsableAPIRenderer, JSONRenderer)
    queryset = Company.objects.all().prefetch_related('funding_rounds', 'funding_rounds__contributions')