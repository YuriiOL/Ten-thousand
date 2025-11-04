"""
URL mapping for the recipe app.
"""
from django.urls import (path, include)
from rest_framework.routers import DefaultRouter
from timer import views

router = DefaultRouter()
router.register('', views.TimerViewSet)

app_name = 'timer'

urlpatterns = [
    path('', include(router.urls)),
]