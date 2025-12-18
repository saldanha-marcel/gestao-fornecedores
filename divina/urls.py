from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from core import views
from users.views import CustomLoginView, CustomPasswordResetView

urlpatterns = [
    path('', views.index, name='index'),
    path('app/', include('core.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('auth/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
