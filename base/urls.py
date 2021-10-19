from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),
    path('', views.feed, name="feed"), 
    path('new-entry/', views.new_entry, name="new-entry"),
    path('my-entries/', views.my_entries, name="my-entries"),
    path('entry/<str:pk>/', views.entry, name="entry"),
    path('edit-entry/<str:pk>/', views.edit_entry, name="edit-entry"),
    path('delete-entry/<str:pk>/', views.delete_entry, name="delete-entry"),
    path('delete-feedback/<str:pk>/', views.delete_feedback, name="delete-feedback"),
]