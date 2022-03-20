from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.awards, name='awards'),
    path('viewawards/<str:pk>/', views.viewawards, name='viewawards'),
    path('addawards/', views.addawards, name='addawards'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]
