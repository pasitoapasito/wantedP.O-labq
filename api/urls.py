from django.urls import path
from api.views   import SeoulOpenDataVeiw

urlpatterns = [
    path('/seoul/sewerlevel-rainfall', SeoulOpenDataVeiw.as_view())
]
