from django.contrib import admin
from recordapp import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recordapp/', include('recordapp.urls')), 
    path('',views.home,name='home') 
]
