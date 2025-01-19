"""
URL configuration for MyTicketStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from EventStore.views import ProjectWorkWelcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectWorkWelcome, name='projectwork_welcome'),
    path('event_manager/', include('EventManager.urls', namespace='event_manager')),
    path('event_shop/', include('EventShop.urls', namespace='event_shop')),
    path('event_store/', include('EventStore.urls', namespace='event_store')),
   
]
urlpatterns += [
     path('accounts/', include('django.contrib.auth.urls')),
     path('accounts/new', include('UsersManager.urls', namespace='users_manager')),
    
]
