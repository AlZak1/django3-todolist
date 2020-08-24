from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def home(request):
    todos = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'todo/home.html', {'todos':todos, 'form':form})


def updatetodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'todo/update.html', {'form':form})


def deletetodo(request, pk):
    item = Todo.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'todo/delete.html', {'item':item})

def orders_app(request):
    return render(request, 'todo/main_app.html')
