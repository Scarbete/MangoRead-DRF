from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns_swagger as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.manga.urls')),
    path('api/v1/users/', include('apps.users.urls')),

]
urlpatterns += doc_urls
