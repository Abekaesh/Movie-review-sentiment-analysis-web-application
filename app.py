from flask import Flask, render_template, request, url_for
from helpers import scrape, analyze_sentiment, save_pie_chart, create_and_save_wordcloud
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        url = request.form.get('url')
        print(url)
        df = scrape(url)
        # Apply sentiment analysis function to the 'reviews' column
        df[['sentiment', 'neg_sentiment_score', 'neu_sentiment_score', 'pos_sentiment_score', 'comp_sentiment_score']] = df['reviews'].apply(analyze_sentiment).apply(pd.Series)
        sorted_df = df.sort_values(by='comp_sentiment_score', ascending=True)
        positives = sorted_df[sorted_df["sentiment"]=="Positive"]["reviews"].tail()
        positive=list(positives)

        neutrals = sorted_df[sorted_df["sentiment"]=="Neutral"]["reviews"].head()
        neutral=list(neutrals)
        
        negatives = sorted_df[sorted_df["sentiment"]=="Negative"]["reviews"].head()
        negative=list(negatives)
        save_pie_chart(df)
        create_and_save_wordcloud(df)
        df.to_csv("movie_reviews_sentiments.csv")
        return render_template('index.html', df=True, positive=positive, neutral=neutral, negative=negative)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)