from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Stand
from .permissions import IsOwnerOrReadOnly
from .serializers import StandSerializer


class StandList(ListCreateAPIView):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer


class StandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Stand.objects.all()
    serializer_class = StandSerializer
