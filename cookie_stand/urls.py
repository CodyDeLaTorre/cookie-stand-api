from django.urls import path
from .views import StandList, StandDetail

urlpatterns = [
    path("", StandList.as_view(), name="stand_list"),
    path("<int:pk>/", StandDetail.as_view(), name="stand_detail"),
]
