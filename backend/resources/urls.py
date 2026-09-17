from django.urls import path
from resources import views

urlpatterns = [
    path('departments/', views.DepartmentListAPIView.as_view(), name='department-list'),
    path('subjects/', views.SubjectListAPIView.as_view(), name='subject-list'),
    path('', views.ResourceListCreateAPIView.as_view(), name='resource-list-create'),
    path('<int:pk>/', views.ResourceDetailAPIView.as_view(), name='resource-detail'),
]