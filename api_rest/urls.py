from django.urls import path, include


urlpatterns = [
    path('', include('api_rest.all_urls.equipments_urls'))
]
