from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('<str:message>/', views.std_list, name='std_list'),
]