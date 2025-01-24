import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Category, Priority, Project, Task, User
from .permissions import IsAdmin, IsEmployee, IsManager
from .serializers import (
    CategorySerializer,
    PrioritySerializer,
    ProjectSerializer,
    TaskSerializer,
    UserSerializer,
)

logger = logging.getLogger(__name__)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsManager]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PriorityViewSet(ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['project', 'priority', 'category']
    search_fields = ['title', 'description']
    permission_classes = [IsEmployee]

    def perform_create(self, serializer):
        logger.info('Creating a new task')
        serializer.save()
