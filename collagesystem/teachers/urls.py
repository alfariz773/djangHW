from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('<str:message>/', views.teach_list, name='teach_list'),
]