from django.urls import path, include

from . import views

app_name = 'user_management'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]
