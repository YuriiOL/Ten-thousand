"""
Serializers for timer API
"""
from rest_framework import serializers

from core.models import Timer

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