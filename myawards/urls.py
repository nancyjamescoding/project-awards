from django.urls import path
from . import views


urlpatterns = [
    path('', views.awards, name='awards'),
    path('viewawards/<str:pk>/', views.viewawards, name='viewawards'),
    path('addawards/', views.addawards, name='addawards'),
]
