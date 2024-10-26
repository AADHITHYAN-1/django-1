from django.shortcuts import render
from .forms import *
from .models import *

def homepage(request):
    data={
        'name':'aadhi',
        'role':'employee',
        'number': [1,2,3,4,5],
        'marks':{'tamil':100,'english':90}
                }
    return render(request,'home.html',data)

def aboutpage(request):
    return render(request, 'about.html')

def SERVICEpage(request):
    return render(request, 'SERVICE.HTML')

def contactpage(request):
    return render(request, 'contact.html')

def productadd(request):
    context={
        'product_form':Product()
    }
    return render(request,'product_add.html', context)