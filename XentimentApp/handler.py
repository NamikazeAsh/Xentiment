import requests
import pandas as pd

def TwitterScraper(hashtag, media_path):
    hashtagName = hashtag
    twitter_data = []
    tweets_per_request = 20  # Number of tweets per request

    payload = {
        'api_key': '81e2e2d6b532db47614567d0eb81462b',
        'query': hashtagName,
        'num': tweets_per_request,
        'result_type': 'recent'
    }

    while len(twitter_data) < tweets_per_request:
        response = requests.get('https://api.scraperapi.com/structured/twitter/search', params=payload)
        data = response.json()
        
        if 'organic_results' in data:
            all_tweets = data['organic_results']
            
            for tweet in all_tweets:
                tweet_url = tweet.get('link', '')
                # Check if the tweet URL contains '/status/' indicating it's an actual tweet
                if '/status/' in tweet_url:
                    twitter_data.append(tweet)

                # Check if we've reached the desired number of tweets
                if len(twitter_data) >= tweets_per_request:
                    break
            
            # Check if there are no more tweets or the API doesn't return more results
            if len(all_tweets) < tweets_per_request:
                break
                
            # Check if 'pagination' exists and get the next page
            if 'pagination' in data and 'next' in data['pagination']:
                payload['page'] = data['pagination']['next']
            else:
                break
        else:
            break  
    df = pd.DataFrame(twitter_data[:tweets_per_request]) 
    df.to_csv(media_path + hashtagName + '.csv', index=False) 

# -------------------------------- TempRunner -------------------------------- #
hashtag = input("Enter hashtag (temp): ")
media_path = "D:/CS/Python/Xentiment/media/"
TwitterScraper(hashtag, media_path)