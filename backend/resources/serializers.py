from rest_framework import serializers
from django.contrib.auth.models import User
from resources.models import Department, Subject, Resource

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField(source='department.code')

    class Meta:
        model = Subject
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    uploaded_by_username = serializers.ReadOnlyField(source='uploaded_by.username')
    subject_code = serializers.ReadOnlyField(source='subject.code')

    class Meta:
        model = Resource
        fields = '__all__'
        read_only_fields = ['uploaded_by', 'download_count', 'created_at']