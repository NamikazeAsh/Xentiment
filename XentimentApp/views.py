from django.shortcuts import render
from django.conf import settings

from XentimentApp.handler import *
from XentimentApp.tweetSentAnal import *

def XentimentHome(request):
    if request.method == 'GET':
        
        query = request.GET.get('searchQuery')
    
        if query:
            
            queryCSV = TwitterScraper(query,settings.MEDIA_ROOT)
            queryCSV = queryCSV + ".csv"
            CSVSentiAnal(queryCSV,queryCSV)
            TweetLinkScraper(queryCSV)    
            print("Analyzed in views")
            
        else:
            
            print("Query: ", query)
        
        # ------------------------------- Final Output ------------------------------- #
        
        
        return render(request,'home.html')
    
    else:
        return render(request,'home.html')
