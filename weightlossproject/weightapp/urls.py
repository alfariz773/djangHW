from django.contrib import admin
from django.urls import path
from weightapp import views  

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-weight/', views.addweight, name='addweight'),
    path('weight-list/', views.weight_list, name='weight_list'),
    path('weight-loss/', views.weight_loss, name='weight_loss'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/',views.delete, name='delete'),
]
