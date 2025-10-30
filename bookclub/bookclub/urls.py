from django.contrib import admin
from clubapp import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubapp/', include('clubapp.urls')),  
    path('',views.sign_up,name='sign'),
]
