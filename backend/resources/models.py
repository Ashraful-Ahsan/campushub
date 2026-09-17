from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100) 
    code = models.CharField(max_length=10)  
    def __str__(self):
        return self.code
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20) 
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')
    semester = models.IntegerField()  
    def __str__(self):
        return f"{self.code} - {self.name}"
class Resource(models.Model):
    RESOURCE_TYPES = [
        ('NOTE', 'Lecture Note'),
        ('QUESTION', 'Question Paper'),
        ('BOOK', 'Book / PDF'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='resources/')
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES, default='NOTE')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='resources')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    download_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title