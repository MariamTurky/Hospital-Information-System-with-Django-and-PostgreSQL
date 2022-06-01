from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def signa(request):
    return render(request , 'accounts/signa.html')

def signd(request):
    return render(request , 'accounts/signd.html') 

def signn(request):
    return render(request , 'accounts/signn.html')  

def signp(request):
    return render(request , 'accounts/signp.html')