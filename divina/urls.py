from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('app/', include('core.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
