from rest_framework import generics, permissions
from .models import Department, Subject, Resource
from .serializers import DepartmentSerializer, SubjectSerializer, ResourceSerializer

class DepartmentListAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SubjectListAPIView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Subject.objects.all()
        dept_id = self.request.query_params.get('department')
        semester = self.request.query_params.get('semester')
        
        if dept_id:
            queryset = queryset.filter(department_id=dept_id)
        if semester:
            queryset = queryset.filter(semester=semester)
        return queryset

class ResourceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Resource.objects.all().order_by('-created_at')
        subject_id = self.request.query_params.get('subject')
        search = self.request.query_params.get('search')
        
        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class ResourceDetailAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer