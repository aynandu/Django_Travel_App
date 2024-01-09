from django.shortcuts import render
from django.http import HttpResponse
from .models import TrainingSectionLayout

# Create your views here.
def demo(request):
   obj=TrainingSectionLayout`.objects.all()`
   return render(request,'index.html',{'result':obj})
'''
def about(request):
   #return HttpResponse("Hello World")
   return render(request,'about.html')

def contact(request):
   return HttpResponse("I'm Contact")
def Result(request):
   val01=int(request.GET['num1']) 
   val02=int(request.GET['num2']) 
   sum=val01+val02
   sub=val01-val02
   mul=val01*val02
   return render(request,'result.html',{'sum':sum,'sub':sub,'mul':mul})
'''