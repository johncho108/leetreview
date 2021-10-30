from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes), path('entries/', views.getEntries), 
    path('entry/<str:pk>/', views.getEntry)
]