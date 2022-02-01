from django.shortcuts import render
from rest_framework import generics
from .serializers import CarDetailSerializer, CarListSerializer
from .models import Car


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
