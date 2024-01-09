import json
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
            linkDict = TweetLinkScraper(queryCSV)    
            print("Analyzed in views")
            
            with open("nAnal.json", 'r+') as file:
                data = json.load(file)
                data['analysis'] += 1
                file.seek(0)
                json.dump(data, file, indent=4)
                
            print(f"The 'analysis' value has been incremented to: {data['analysis']}")
            
            
            context = {
                'linkDict':linkDict,
                'nAnalData':data,
            }
            return render(request,'home.html',context=context)
            
        else:
            
            with open("nAnal.json", 'r+') as file:
                data = json.load(file)
            
            context = {
                'nAnalData':data,
            }
            return render(request,'home.html',context=context)
    else:
        context = {
                'nAnalData':data,
            }
        return render(request,'home.html',context=context)
