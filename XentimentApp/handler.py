import requests
import pandas as pd

def TwitterScraper(hashtag):

    hashtagName = hashtag
    twitter_data = []
    
    payload = {
        'api_key': '81e2e2d6b532db47614567d0eb81462b',
        'query':hashtagName,
        'num':20,
        'result_type':'recent'
    }    

    response = requests.get(
        'https://api.scraperapi.com/structured/twitter/search',params=payload
    )
    
    data = response.json()
    all_tweets = data['organic_results']
    for tweet in all_tweets:
        twitter_data.append(tweet)
        
    df = pd.DataFrame(twitter_data)
    df.to_csv(hashtagName +'.csv',index=True)
    
    
