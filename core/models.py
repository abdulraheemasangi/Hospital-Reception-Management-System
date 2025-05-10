from django.db import models

# Create your models here.


class patient_register(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    aadhaar_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    health_problem = models.TextField()
    date_of_visit = models.DateField(auto_now_add=True)

    