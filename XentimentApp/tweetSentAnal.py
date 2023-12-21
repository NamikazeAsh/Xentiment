import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import pandas as pd

def CalcSentiScore(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    return scores['compound']

def CSVSentiAnal(input_file_path, output_file_path):
    df = pd.read_csv(input_file_path)

    df['sentiment_score'] = df['snippet'].apply(CalcSentiScore)

    df.to_csv(output_file_path, index=True)
    # print("analyzed")


    
    
# # ----------------------------- Temp Code Runner ----------------------------- #
# input_file_path = 'D:/CS/Python/Xentiment/#.csv'
# output_file_path = input_file_path
# CSVSentiAnal(input_file_path, output_file_path)

