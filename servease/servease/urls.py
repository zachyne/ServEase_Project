"""
URL configuration for servease project.

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

from django.conf import settings 
from django.conf.urls.static import static

from pages import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('signup/', views.signup_page, name='sign_up'),
    path('login/', views.login_page, name='log_in'),
    path('logout/', views.logout_user, name='logout'),
    path('about/', views.about, name='about'), 
    path('mainpage/', views.main_page, name='main_page'),
    path('browse/', views.browse_page, name='browse'),
    #path('browse/', views.browse_page, name='service_detail'),
    path('services/', include('services.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
