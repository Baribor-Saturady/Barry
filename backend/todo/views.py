from django.shortcuts import render

# Create your views here.

def index(request):
    """
    returns the index page for the url todo/
    """
    return render(request, 'todo/index.html',{'message':'Welcome to the index page'})

def create_todo(request):
    "return the create todo page"
    return render(request, 'todo/create.html',{'message':"How do you want to create your todo"})