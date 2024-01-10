from rest_framework.generics import ListCreateAPIView
from project.models import Refback
from project.serializers import RefbackSerializer


class RefbackListGenericView(ListCreateAPIView):
    queryset = Refback.objects.all()
    serializer_class = RefbackSerializer
