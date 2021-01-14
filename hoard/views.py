from django.shortcuts import render

def index(request):
    return render(request, 'hoard/index.html')
