from django.urls import path
from ..views import EquipmentCreateListView, EquipmentRetriveUpdateDestroyView


urlpatterns = [
  path(
    'equipments/',
    EquipmentCreateListView.as_view(),
    name='equipments-create-list'
  ),
  path(
    'equipments/<uuid:pk>/',
    EquipmentRetriveUpdateDestroyView.as_view(),
    name='equipments-detail-view'
  )
]
