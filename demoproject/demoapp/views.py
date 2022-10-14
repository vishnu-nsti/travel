from django.http import HttpResponse
from django.shortcuts import render

from . models import place
from .models import team

# Create your views here.


def demov(request):
    obj=place.objects.all()
    mem=team.objects.all()
    return render(request,'index.html',{'result':obj,'res':mem})

# def demov(request):
#     name='India'
#     return render(request,'index.html',{'obj':name})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     z=x+y
#     return render(request,'result.html',{'result':z})

# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return render(request,'contact.html')
