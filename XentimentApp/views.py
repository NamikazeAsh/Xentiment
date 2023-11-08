from django.shortcuts import render

# Create your views here.
def XentimentHome(request):
    return render(request,'home.html')