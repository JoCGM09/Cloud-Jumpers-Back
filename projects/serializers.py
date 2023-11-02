from rest_framework import serializers
from projects.models import Project

class ProjectSerializer(serializers. ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','dni', 'antecedentes_patologicos', 'antecedentes_quirurgicos', 'rams', 'relato_cronologico','plan', 'created_at')
        read_only_fields = ('created_at', )