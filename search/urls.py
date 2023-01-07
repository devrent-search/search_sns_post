from django.urls import path

from search import views

urlpatterns = [
    path('search/', views.search, name='temp1'),
    path('', views.index)
]