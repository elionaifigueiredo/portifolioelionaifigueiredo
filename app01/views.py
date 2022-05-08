from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def base2(request):
    return render(request,'base2.html')

def projetos(request):
    return render(request,'projetos.html')

def parceiros(request):
    return render(request,'parceiros.html')

