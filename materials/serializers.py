from rest_framework import serializers

from .models import Category, Material


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model: Category
        fields: "__all__"


class MeterialSerializer(serializers.ModelSerializer):
    class Meta:
        model: Material
        fields: "__all__"
