"""
URL configuration for myproject project.

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
from django.urls import path, include
from myapp_les3.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('myapp.urls')),
    path('myapp_2/', include('myapp_2.urls')),
    path('les3/', include('myapp_les3.urls')),
    path('', index),
    path('les4/', include('myapp_les4.urls')),
    path('sem3/', include('myapp_sem3.urls')),
    path('sem4/', include('myapp_sem4.urls')),
    # path('__debug__/', include('debug_toolbar.urls')),
    path('les6/', include('myapp_les6.urls')),
]