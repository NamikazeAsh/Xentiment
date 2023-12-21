from django.shortcuts import render
from django.conf import settings

from XentimentApp.handler import *
from XentimentApp.tweetSentAnal import *

def XentimentHome(request):
    if request.method == 'GET':
        
        query = request.GET.get('searchQuery')
    
        # -------------------------- Retrieval from handler & save as CSV -------------------------- #
        if query:
            queryCSV = TwitterScraper(query,settings.MEDIA_ROOT)
            print("Query: ", query)
            print(queryCSV)
        else:
            print("Query: ", query)
        
        # ---------------------------- Sentiment Analysis ---------------------------- #
        CSVSentiAnal(queryCSV,queryCSV)
        print("Analyzed in views")
        
        
        # ------------------------------- Final Output ------------------------------- #
        
        
        return render(request,'home.html')
    
    else:
        return render(request,'home.html')
