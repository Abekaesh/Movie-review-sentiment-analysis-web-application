# Movie Review Sentiment Analysis Web Application

## Overview

This Flask-based web application allows users to analyze movie critic reviews from Rotten Tomatoes. By providing a Rotten Tomatoes URL, the app scrapes the reviews, performs sentiment analysis on each one, and visualizes the results. The output includes a word cloud of the reviews, a pie chart showing the distribution of positive, negative, and neutral reviews, and displays the top 5 reviews for each sentiment category.

## Features

- **Web Scraping**: Extracts movie critic reviews from Rotten Tomatoes using Edge for web scraping.
- **Sentiment Analysis**: Analyzes each review to determine if it's positive, negative, or neutral.
- **Visualization**:
  - **Word Cloud**: Generates a word cloud to highlight the most frequent words in the reviews.
  - **Pie Chart**: Displays the proportion of positive, negative, and neutral reviews.
  - **Top Reviews**: Shows the top 5 positive, negative, and neutral reviews.

## Technologies Used

- **Backend**: Flask
- **Web Scraping**: Edge browser
- **Sentiment Analysis**: VADER
- **Visualization**: Matplotlib, WordCloud

## Requirements

- **Python 3.x**
- **Flask**
- **Edge browser**
- **Selenium** (for web scraping with Edge)
- **Matplotlib**
- **WordCloud**
- **NLTK**

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/moviereview-sentiment-analysis.git
    cd moviereview-sentiment-analysis
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Edge Driver**:
    - Download the Edge WebDriver that matches your Edge browser version from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
    - Place the WebDriver executable in your system PATH or in the project directory.

## Usage

1. **Run the Application**:
    ```sh
    python app.py
    ```

2. **Access the Web Application**:
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Analyze Reviews**:
    - Enter the Rotten Tomatoes URL of the movie you want to analyze.
    - Click the "Analyze" button.
    - View the sentiment analysis results including the word cloud, pie chart, and top reviews.

## Compatibility

- The application is compatible with any modern web browser, but it uses Edge for web scraping.

## Target Audience

- **Movie Enthusiasts**: Get insights into the general sentiment of movie critic reviews.
- **Data Analysts**: Analyze and visualize sentiment data from reviews.
- **Developers**: Learn how to integrate web scraping, sentiment analysis, and data visualization in a web application.

## Advantages

- **Automated Review Analysis**: Saves time by automating the extraction and analysis of movie reviews.
- **Visual Insights**: Provides visual representations of data, making it easier to understand the sentiment distribution.
- **Top Reviews Highlighted**: Quickly access the most impactful reviews, categorized by sentiment.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
