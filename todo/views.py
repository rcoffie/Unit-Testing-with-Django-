from django.shortcuts import render, redirect
from todo.models import Todo
from todo.forms import TodoForm
# Create your views here.


def list(request):
    todo = Todo.objects.all()
    context = {'todo':todo,}

    return render(request, 'index.html',context)


def list_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {'todo':todo}
    return render (request, 'detail.html',context)

def create_todo(request):
    create_form = TodoForm()
    if request.method == 'POST':
        create_form = TodoForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('list')
        else:
            create_form = TodoForm()
    context = {'create_form':create_form,}

    return render(request, 'create.html',context)


def update_todo(request, id):
    todo = Todo.objects.get(id=id)
    update_form = TodoForm(instance=todo)
    if request.method == 'POST':
        update_form = TodoForm(request.POST, instance=todo)
        if update_form.is_valid():
            update_form.save()
            return redirect('list')
        else:
            update_form = TodoForm(instance=todo)
    context = {'update_form':update_form}

    return render(request, 'update.html',context )

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('list')
