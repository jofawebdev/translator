from django.urls import path
from . import views


urlpatterns = [
    path('', views.translate_text, name='translate_text'),
    path('logout/', views.logout_view, name='logout'),
]