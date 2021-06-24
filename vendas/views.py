from django.shortcuts import render
from rest_framework import viewsets
from vendas.serializers import VendaSerializer, VendaItensSerializer
from vendas.models import Venda, VendaItens


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaItensViewSet(viewsets.ModelViewSet):
    queryset = VendaItens.objects.all()
    serializer_class = VendaItensSerializer

def home(request):
    return render(request, 'home.html')
