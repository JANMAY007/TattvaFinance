from .views import Scanner, LoginView
from django.urls import path

urlpatterns = [
    path('scanner/', Scanner.as_view(), name='scanner'),
    path('login/', LoginView.as_view(), name='login'),
]
