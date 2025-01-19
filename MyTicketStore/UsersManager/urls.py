from django.urls import path
from .views import register_new_user
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users_manager'
urlpatterns = [
    path('register/', register_new_user, name='register_new_user'),
    
]