from django.shortcuts import render, redirect

from .models import ToDo
from .forms import ToDoForm

# Create your views here.

def all_todo(request):
    form = ToDoForm()
    todos = ToDo.objects.order_by('-date_added')
    return render(request, 'todo/all_todo.html', {'todos': todos, 'form': form})

def add(request):
    if request.method == 'POST':
        td = ToDoForm(request.POST)
        if td.is_valid():
            tdnew = td.save()
    return redirect('todo:all_todo')

def delete_todo(request, todo_id):
    td = ToDo.objects.get(id=todo_id)
    td.delete()
    return redirect('todo:all_todo')

def change_status(request, todo_id):
    td = ToDo.objects.get(id=todo_id)
    td.done = not td.done
    td.save()
    return redirect('todo:all_todo')
