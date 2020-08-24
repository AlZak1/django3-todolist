from rest_framework.generics import ListAPIView
from .serializers import TodoSerializer
from ..models import Todo

class TodoListAPIView(ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
