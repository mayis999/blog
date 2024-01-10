from rest_framework import serializers

from project.models import Project, Refback, Insurance


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class RefbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refback
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'