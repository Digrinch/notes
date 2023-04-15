from django.urls import path, include
from rest_framework import routers
from api.views import TasksViewSet
from api.apps import ApiConfig


app_name = ApiConfig.name

router = routers.DefaultRouter()
router.register('tasks', TasksViewSet)

urlpatterns = [
    path('', include(router.urls))
]
