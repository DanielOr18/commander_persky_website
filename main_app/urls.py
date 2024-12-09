from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game-details/', views.game_details, name='game_details'),
    path('faq-and-tips/', views.faq, name='faq'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('support/', views.support, name='support'),
    path('download/', views.download, name='download'),
]
