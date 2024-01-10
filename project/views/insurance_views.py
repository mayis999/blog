from rest_framework.generics import ListCreateAPIView
from project.models import Insurance
from project.serializers import InsuranceSerializer


class InsuranceListGenericView(ListCreateAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer