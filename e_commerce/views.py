from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'e_commerce/publica/index.html')
