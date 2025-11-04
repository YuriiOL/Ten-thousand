"""
Views for the timer APIs
"""
from rest_framework import (viewsets, mixins)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (Timer, Category)
from timer import serializers

class TimerViewSet(viewsets.ModelViewSet):
    """Views for manage timer APIs"""
    serializer_class = serializers.TimerDetailSerializer
    queryset = Timer.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        """Restrict timer to an authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.TimerSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new timer."""
        serializer.save(user=self.request.user)

class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Views for manage category APIs"""
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        """Restrict category to an authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

