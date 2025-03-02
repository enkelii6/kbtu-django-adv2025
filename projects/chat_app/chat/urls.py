from django.contrib.auth.views import LoginView
from django.urls import path

from chat import views

urlpatterns = [
    path('', views.chat_page, name='chat-page'),
    path('auth/login/', LoginView.as_view(template_name='chat/LoginPage.html'), name='login-user'),
    path('auth/logout/', views.custom_logout, name='logout-user'),
]
