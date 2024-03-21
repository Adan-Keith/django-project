"""
URL configuration for locallibrary2 project.

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
# This code snippet is the URL configuration for a Django project. Let me break it down for you:
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]

# from django.contrib.auth import views as auth_views
# urlpatterns = [
#     # Other URL patterns...
#     path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     # Other URL patterns...
# ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#use include() to add paths from the catalog application


# urlpatterns = [
#         path('catalog/', include('catalog.urls')),
# ]

#Add URL maps to redirect the base URL to our application

# urlpatterns = [
#     path('', RedirectView.as_view(url='catalog/', permanent=True)),
    
# ]

#Using static() to add URL mapping to server stattic files during development only. like css and js files and images


# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)