from django.shortcuts import render
from . models import  student
from . forms import  DataForm
from . forms import modelform
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

l=[]
def first(reqeust):
    res=student.objects.all().filter(sid=100)



    return render(reqeust,'home.html',context={'result':res})

def contact(request):
    form=DataForm()
    return render(request,'home.html',{'form':form})
def modelfrm(request):
    form = modelform()
    return render(request, 'home.html', {'form': form})





def getdata(request):
    try:
        data = student.objects.get(sid=12)
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse(data)
