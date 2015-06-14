__author__ = 'song'

from .models import Merlot

from .serializers import MerlotSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
class MerlotListAPIView(ListCreateAPIView):
    #model = Merlot
    queryset = Merlot.objects.all()
    serializer_class = MerlotSerializer
    filter_fields = ('name', 'description')

class MerlotDetailAPIView(RetrieveUpdateAPIView):
    queryset = Merlot.objects.all()
    #model = Merlot
    serializer_class = MerlotSerializer
'''
class MerlotList(APIView):
    def get(self, request, format=None):
        merlots = Merlot.objects.all()
        serialized_merlots = MerlotSerializer(merlots, many=True)
        filter_fields = ('name',)
        return Response(serialized_merlots.data)

class MerlotDetail(APIView):

    def get_object(self, id):
        try:
            return Merlot.objects.get(id=id)
        except Merlot.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        merlot = self.get_object(id)
        serialized_merlot = MerlotSerializer(merlot)
        return Response(serialized_merlot.data)

    '''