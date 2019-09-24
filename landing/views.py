from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from landing.models import Heroi, Universo, Habilidade, Arg_vilao
from landing.serializers import HeroiSerializer, UniversoSerializer, HabilidadeSerializer, ArgVilaoSerializer


class HeroiViewSet(viewsets.ModelViewSet):
    queryset = Heroi.objects.all()
    serializer_class = HeroiSerializer


class UniversoViewSet(viewsets.ModelViewSet):
    queryset = Universo.objects.all()
    serializer_class = UniversoSerializer


class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer


class VilaoViewSet(viewsets.ModelViewSet):
    queryset = Arg_vilao.objects.all()
    serializer_class = ArgVilaoSerializer
