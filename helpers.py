import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from wordcloud import WordCloud

nltk.download('vader_lexicon')
nltk.download('stopwords')

import matplotlib.pyplot as plt

def create_and_save_wordcloud(df):
    text = ' '.join(df["reviews"])
    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)
    
    # Save the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig("./static/images/wordcloud.jpg")
    plt.close()

def save_pie_chart(df):
    labels = ['Negative', 'Neutral', 'Positive']
    
    df["sentiment"].value_counts().plot(kind="pie", autopct="%.1f%%")
    
    plt.savefig("./static/images/pie_chart.jpg")
    plt.close()

def scrape(url):
    reviews = []
    driver = webdriver.Edge(options=webdriver.EdgeOptions())
    driver.get(url)
    while True:
        try: 
            contents = driver.find_elements(By.CLASS_NAME, "review-text")
            for content in contents:
                review = content.get_attribute("outerHTML")
                reviews.append(review)
            driver.find_element(By.CSS_SELECTOR, "rt-button.next").click()
            time.sleep(3)
        except:
            print("Scraping completed")
            break
    df = pd.DataFrame()
    df["reviews"] = reviews
    df["reviews"] = df["reviews"].str.replace("<p class=\"review-text\" data-qa=\"review-quote\">","")
    df["reviews"] = df["reviews"].str.replace("<p slot=\"content\" class=\"audience-reviews__review js-review-text\" data-qa=\"review-text\">\n                        ","")
    df["reviews"] = df["reviews"].str.replace("</p>","")
    return df

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    # Join the words back into a cleaned text
    cleaned_text = ' '.join(words)
    
    return cleaned_text

def analyze_sentiment(review):
    cleaned_review = clean_text(review)
    
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(cleaned_review)
    neg = sentiment_scores['neg']
    neu = sentiment_scores['neu']
    pos = sentiment_scores['pos']
    
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, neg, neu, pos, compound_score

