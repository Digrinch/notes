from rest_framework import viewsets
from tasks.models import Task
from api.serializers import TaskSerializer

# Create your views here.
class TasksViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
