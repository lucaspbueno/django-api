# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from rest_framework import generics
from ..models import Equipment
from ..serializers import EquipmentSerializer


class EquipmentCreateListView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
