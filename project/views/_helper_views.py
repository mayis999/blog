from django.contrib.auth.mixins import AccessMixin
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from project.serializers import ProjectSerializer

"""
parser: Incoming data(json) into Python native datatype(dict/list): JSON to Python datatype
renderer: Python datatype into JSON: Python datatype to JSON
"""


@api_view(http_method_names=['GET', 'POST'])
def project_list_or_create(request):
    if request.method == 'GET':
        projects = Project.objects.all()

        serializer = ProjectSerializer(
            instance=projects,
            many=True,
        )

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    else:
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )


@api_view(http_method_names=['GET', 'PUT', 'PATCH', 'DELETE'])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'GET':

        serializer = ProjectSerializer(
            instance=project,
        )

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    elif request.method == 'PUT':

        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(
            instance=project,
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )
    elif request.method == 'PATCH':
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(
            instance=project,
            data=request.data,
            partial=True,
        )
        serializer.is_valid()
        serializer.save()
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )
    else:
        project = get_object_or_404(Project, pk=pk)
        project.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()

        serializer = ProjectSerializer(
            instance=projects,
            many=True
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    head = get

    def post(self, request):
        serializer = ProjectSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )


class ProjectDetailView(APIView):

    def _check_request_ip_address(self, request) -> bool:
        # check if the IP address is valid
        return True or False

    def setup(self, request, *args, **kwargs):
        # Initialize custom attributes which are shared between all views
        super().setup(request, *args, **kwargs)

        if request.method == 'GET':
            name = 'M'
        elif request.method == 'PUT':
            name = 'K'
        else:
            name = 'X'
        self.name = name

    def dispatch(self, request, *args, **kwargs):
        # Do something before calling views
        is_valid = self._check_request_ip_address(request)
        if not is_valid:
            return Response(
                'The request has been blocked',
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        super().dispatch(request, *args, **kwargs)

    def filter_projects_by_name(self, name=None):
        name = name or self.name
        projects = Project.objects.filter(name_icontains=name)

        return projects

    def get(self, request, pk, format=None):
        projects = self.filter_projects_by_name()
        project = get_object_or_404(projects, pk=pk)


        serializer = ProjectSerializer(
            instance=project
        )

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        projects = self.filter_projects_by_name()
        project = get_object_or_404(projects, pk=pk)


        serializer = ProjectSerializer(
            instance=project,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

    def patch(self, request, pk):
        project = get_object_or_404(Project, pk=pk)

        serializer = ProjectSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

    def patch(self, request, pk):
        projects = self.filter_projects_by_name()
        project = get_object_or_404(projects, pk=pk)
        serializer = ProjectSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

    def delete(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        project.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

from django.views.generic.list import ListView
from project.models import Project


class RestrictBlockedIPAddressesMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        client_ip = self.get_client_ip_address()
        ip_blocked_lst = self.get_blocked_ip_addresses()
        if client_ip in ip_blocked_lst:
            return Response(data='error')
        return super().dispatch(request, *args, **kwargs)

    def get_client_ip_address(request):
        req_headers = request.META
        x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for_value:
            ip_addr = x_forwarded_for_value.split(',')[-1].strip()
        else:
            ip_addr = req_headers.get('REMOTE_ADDR')
        return ip_addr

    def get_blocked_ip_addresses(self):
        ip_blocked_lst = ["192.168.1.1"]

        return ip_blocked_lst
