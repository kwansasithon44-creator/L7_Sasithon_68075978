from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>ICT12367 SPU</h1>")

def contact(request):
    return HttpResponse("<h1>ติดต่อ 68075978 Sasithon Saoprakhon</h1>")

def form(request):
    return render(request, 'form.html')