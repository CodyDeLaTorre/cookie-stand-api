from django.urls import path
from .views_front import (
    StandCreateView,
    StandDeleteView,
    StandDetailView,
    StandListView,
    StandUpdateView,
)

urlpatterns = [
    path("", StandListView.as_view(), name="stand_list"),
    path("<int:pk>/", StandDetailView.as_view(), name="stand_detail"),
    path("create/", StandCreateView.as_view(), name="stand_create"),
    path("<int:pk>/update/", StandUpdateView.as_view(), name="stand_update"),
    path("<int:pk>/delete/", StandDeleteView.as_view(), name="stand_delete"),
]
