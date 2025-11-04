from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('pdf/<int:pk>/', views.generate_pdf, name='generate_pdf'),
    path('email/<int:pk>/', views.send_product_email, name='send_product_email'),
]
