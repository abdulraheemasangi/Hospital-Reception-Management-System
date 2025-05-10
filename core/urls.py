from django.urls import path
from core import views



urlpatterns = [

    path('',views.home,name='home'),
    path('patient_register/',views.patient_register_form,name='patient_register'),
    path('patient_list/',views.patient_list,name='patient_list'),
    path('patient_details/<int:pk>/', views.patient_details, name='patient_details'),
    path('about/', views.about, name='about'),



]
