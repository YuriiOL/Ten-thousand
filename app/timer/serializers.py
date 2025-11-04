"""
Serializers for timer API
"""
from rest_framework import serializers

from core.models import (Timer, Category)

class TimerSerializer(serializers.ModelSerializer):
    """Serializer for Timer"""

    class Meta:
        model = Timer
        fields = ['id', 'title', 'description', 'last_time', 'total_time']
        read_only_fields = ['id']

class TimerDetailSerializer(TimerSerializer):
    """Serializer for timer detail view."""

    class Meta(TimerSerializer.Meta):
        fields = TimerSerializer.Meta.fields + ['description']

class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category view."""

    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']