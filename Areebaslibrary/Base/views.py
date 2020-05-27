from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Base/index.html')
def home2(request):
    return render(request, 'Base/homepage2.html')
