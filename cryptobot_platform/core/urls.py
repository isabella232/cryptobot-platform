from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('create-bot/', views.create_bot, name="create_bot"),
    path('start-bot/<str:id>', views.start_bot, name="start_bot"),
    path('stop-bot/<str:id>', views.stop_bot, name="stop_bot"),
    path('bot-list/', views.bot_list, name="bot_list")
]
