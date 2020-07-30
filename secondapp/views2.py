from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

# Create your views here.
def index1(request):
    return HttpResponse('index1')

def mini(request):
    return HttpResponse('mini!')

def hos(request):
    hospital = Hospital.objects.all()
    return render(request,'show2 copy.html',{'list':hospital})
  #  html=''
  #  for c in hospital:
  #      html += '%s %s <br>'% (c.id, c.name)
  #  print(hospital)
  #  return HttpResponse(html)