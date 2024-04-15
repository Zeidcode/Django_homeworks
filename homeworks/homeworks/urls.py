from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homework_1.urls')),
   # path('__debug__/', include("debug_toolbar.urls")),
]
