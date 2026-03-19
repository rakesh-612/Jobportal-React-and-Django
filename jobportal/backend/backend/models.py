from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    title=models.CharField(null=True, max_length=200)
    description=models.TextField(null=True, max_length=300)
    company=models.CharField(null=True, max_length=100)
    location=models.CharField(null=True, max_length=100)
    salary=models.CharField(blank=True, max_length=100)
    posted_on=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)

class Application(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired')
    )
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(default='pending', max_length=20, choices=STATUS_CHOICES)
    location=models.CharField(null=True, max_length=100)
    applied_on=models.DateField(auto_now_add=True)
