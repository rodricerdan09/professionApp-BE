from django.urls import path, include
from .views import UserDetailView
from django.contrib.auth import urls


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('misdatos/<int:pk>', UserDetailView.as_view(), name='user-detail'),

]
