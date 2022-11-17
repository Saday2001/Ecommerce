from django.urls import path
from .views import *
app_name='user'

urlpatterns = [
    path('register/', UserRegister, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contact/', Contact_view, name = 'contact_view')
    
]