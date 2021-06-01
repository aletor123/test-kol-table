from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import KolListSerializer, KolCreateSerializer
from apps.kol.models import Kol


class KolViewSet(ModelViewSet):
    queryset = Kol.objects.all()
    serializer_class = KolListSerializer
    serializer_class_mapping = {
        'create': KolCreateSerializer,
        'update': KolCreateSerializer,
        'partial_update': KolCreateSerializer,
    }

    def get_serializer_class(self):
        if self.action in self.serializer_class_mapping:
            return self.serializer_class_mapping[self.action]
        return super().get_serializer_class()

    @action(methods=['get'], detail=False)
    def specialties(self, request):
        specialties = Kol.objects.distinct('specialty').values_list(
            'specialty', flat=True
        )
        return Response({
            'specialties': specialties
        })

