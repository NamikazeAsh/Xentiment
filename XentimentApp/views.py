from django.shortcuts import render

# Create your views here.
def XentimentHome(request):
    if request.method == 'GET':
        query = request.GET.get('searchQuery')
        print("Query: ", query)
    return render(request,'home.html')
