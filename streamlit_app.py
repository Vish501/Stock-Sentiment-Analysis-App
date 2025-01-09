import streamlit as st
from transformers import pipeline

# Creating the sentiment analysis pipeline
classifier = pipeline(task='text-classification', model='ProsusAI/finbert')


def feed(ticker):
    rss_url = f'https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&lang=en-US'
    return feedparser.parse(rss_url)


def main():
    st.title('#📈 TICKER SENTIMENET ANALYZER')
    st.write('Enter a ticker and get the news sentiment for it.')

    if prompt := st.chat_input("Ticker"):
        pass



if __name__ == '__main__':
    main()
