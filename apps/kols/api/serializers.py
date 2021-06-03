from rest_framework import serializers

from apps.kols.models import Kol


class KolListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Kol
        fields = ('full_name', 'specialty')


class KolCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kol
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'credential',
            'specialty',
        )
