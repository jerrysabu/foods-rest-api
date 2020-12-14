from rest_framework import serializers
from . models import Category, Food

from . import models


class CategorySerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
            model = Category
            fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
            model = Food
            fields = '__all__'
