from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from social_auth.views import home , chat_interface_view, chatbot_api_view



urlpatterns = [
    path('', home, name='home'),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('chat/', chat_interface_view, name='chat_interface'),
    path('api/chatbot/', chatbot_api_view, name='chatbot_api'),

    

]
