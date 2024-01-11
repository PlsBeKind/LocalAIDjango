from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ai_model/', include('ai_model.urls')),
    path('plugins/spotify/', include('plugins.spotify.urls')),
]