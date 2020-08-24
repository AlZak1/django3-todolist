from django.urls import path
from .api_views import TodoListAPIView

urlpatterns = [
    path('todos/', TodoListAPIView.as_view(), name='todos')
]
