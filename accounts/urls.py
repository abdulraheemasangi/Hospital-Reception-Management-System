from django.urls import path
from . import views



urlpatterns = [

    path('',views.login_,name='login_'),
    path('register_/',views.register_,name='register_'),
    path('logout_/',views.logout_,name='logout_'),
    path('profile',views.profile,name='profile'),
    path('changepass',views.changepass,name='changepass'),
    path('update_profile/',views.update_profile,name='update_profile'),

]
