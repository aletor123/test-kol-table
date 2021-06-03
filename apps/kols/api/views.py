from rest_framework.viewsets import ModelViewSet

from .serializers import KolListSerializer, KolCreateSerializer
from apps.kols.models import Kol


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

