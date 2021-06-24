from django.db import router
from django.urls.conf import path
from django.views.generic import base
from rest_framework.routers import DefaultRouter
from vendas.views import VendaViewSet, VendaItensViewSet, home

router = DefaultRouter()

router.register(r'vendas', VendaViewSet, basename='vendas')
router.register(r'venda_itens', VendaItensViewSet, basename='vendas_itens')

urlpatterns = router.urls

urlpatterns_home = [
    path('', home)
]

