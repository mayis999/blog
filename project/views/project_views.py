from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework import mixins, status

from project.models import Project
from project.serializers import ProjectSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ProjectDetailGenericView(
    RetrieveUpdateDestroyAPIView
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectListGenericView(
    ListCreateAPIView
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

