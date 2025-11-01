from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('logapi/', include('logapi.urls')),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('logapi/', include('logapi.urls')),  
# ]
