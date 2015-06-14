__author__ = 'song'

from .models import Merlot

from rest_framework import serializers


class MerlotSerializer(serializers.ModelSerializer):

    haha = serializers.SerializerMethodField()

    def get_haha(self, obj):
        return "haha said"

    lala = serializers.SerializerMethodField()

    def get_lala(self, obj):
        return "lala"

    class Meta:
        model = Merlot
        fields = (
            'id',
            'name',
            'size',
            'price',
            'description',
            'haha',
            'lala',
        )