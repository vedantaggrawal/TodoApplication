from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Tasks
# Create your views here.

def index(request):
     context = {'todo_list' : Tasks.objects.all()}
     return render(request, 'todo/index.html', context)
    
def add(request):
    todo = Tasks(content = request.POST['content'])
    todo.save() 
    return redirect('/todo/')

def delete(Request,todo_id):
    todo = Tasks.objects.get(id=todo_id)
    todo.delete()
    return redirect('/todo/')