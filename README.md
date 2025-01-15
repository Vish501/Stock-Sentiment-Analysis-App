# 📈 Stock News Sentiment Analyzer

This Python application analyzes the sentiment of news related to a specific stock using the Yahoo Finance 2.0 RSS feed. 

Deployed on: https://stock-sentiment-analysis-app.streamlit.app/

**Key Features:**

* **Streamlit UI:** User-friendly interface for inputting stock ticker and filter keywords.
* **Yahoo Finance RSS Feed:** Retrieves real-time news related to the input stock.
* **News Filtering:** Filters news articles based on the provided keywords.
* **Sentiment Analysis:** Analyzes the sentiment of filtered news articles.
* **Result Visualization:** Displays the overall sentiment (positive, negative, or neutral) based on the sentiment analysis score.

## How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
