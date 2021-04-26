from django.shortcuts import render

# Create your views here.

def index(request):
    """
    returns the index page for the url todo/
    """
    return render(request, 'todo/index.html',{'message':'Welcome to the index page'})
