from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'Vansh'})


def add(request):
    value1 = request.POST['num1']
    value2 = request.POST['num2']
    result = int(value1) + int(value2)
    return render(request, 'result.html', {'result': result})
