from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('add-note/', views.add_note),
    path('notes/', views.list_notes),
]