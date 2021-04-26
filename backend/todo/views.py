from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'todo/index.html',{'message':'Welcome to the index page'})
