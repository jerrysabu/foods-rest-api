from django.shortcuts import render
from rest_framework import generics, filters
from . models import Food
from . serializers import FoodSerializer
# Create your views here.

class FoodAPIView(generics.ListCreateAPIView):

    search_fields = ['name','price']
    filter_backends = (filters.SearchFilter,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
