from django.shortcuts import render

# Create your views here.


def basedir(request):

    return render(request, 'blogapp/base.html')


def homepage(request):

    return render(request, 'blogapp/home.html')
