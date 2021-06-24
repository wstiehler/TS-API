from django.contrib import admin
from django.urls import path, include
from vendas.urls import urlpatterns, urlpatterns_home


urlpatterns = [
    path('', include(urlpatterns_home)),
    path('admin/', admin.site.urls),
    path('api/', include(urlpatterns))
]
