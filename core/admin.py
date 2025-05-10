from django.contrib import admin
from .models import patient_register

# Register your models here.
class registerAdmin(admin.ModelAdmin):

    list_display=['full_name','phone_number','address','age','gender','state','aadhaar_number','email','health_problem','date_of_visit']

admin.site.register(patient_register,registerAdmin)

# Username : Admin
# Password : Admin@123