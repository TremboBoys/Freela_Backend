from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.project.models import Project

class ProjectSerializer(ModelSerializer):
    specific_data = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = "__all__"

    def get_specific_data(self, obj):
        return [obj.theme, obj.title, obj.context]
        