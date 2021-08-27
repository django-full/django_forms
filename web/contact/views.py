from django.shortcuts import render

from . import forms


# Create your views here.

def index(request):
    form = forms.Post()
    context ={
    'Forms':form
    }

    return render(request,'index.html',context)


def contact(request):
    form = forms.Contact()
    context ={
        'Forms':form
    }
    print(request.POST)
    return render(request,'contact.html',context)