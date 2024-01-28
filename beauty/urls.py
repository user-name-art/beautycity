"""
URL configuration for beauty project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from beautycityapp import views, masters, slots, order
from beautycityapp.views import UserRegistrationView, UserLoginView, OTPVerificationView


urlpatterns = [
    path('admin_panel/', admin.site.urls),
    path('', views.show_home_page, name='main'),
    path('service/', views.show_service),
    path('admin/', views.show_admin),
    path('notes/', views.show_notes),
    path('popup/', views.show_popup),
    path('service_finally/', views.show_service_finally),
    path('service/masters', masters.get_masters),
    path('service/slots', slots.get_slots),
    path('service/order', order.make_order),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('verify-otp/', OTPVerificationView.as_view(), name='otp_verification'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
