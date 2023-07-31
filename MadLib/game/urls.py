from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pickGame/<int:id>', views.pickGame, name='pickGame'),
    path('checkInputs/', views.checkInputs, name='checkInputs'),
    path('storyMaker/<str:filled_story>/<str:story_title>/', views.storyMaker, name='storyMaker'),
]

