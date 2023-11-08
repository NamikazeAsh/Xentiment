import requests
import pandas as pd

def TwitterScraper(hashtag,ntweets,media_path):

    hashtagName = hashtag
    twitter_data = []
    
    payload = {
        'api_key': '81e2e2d6b532db47614567d0eb81462b',
        'query':hashtagName,
        'num':ntweets+1,
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
    df.to_csv(media_path + hashtagName +'.csv',index=True)


# -------------------------------- TempRunner -------------------------------- #
hashtag = input("Enter hashtag (temp): ")
ntweets = int(input("Number of tweets: "))
media_path = "D:/CS/Python/Xentiment/media/"
TwitterScraper(hashtag,ntweets,media_path)

