import feedparser
import streamlit as st
from transformers import pipeline
import yfinance as yf


# Creating the sentiment analysis pipeline
classifier = pipeline(task='text-classification', model='ProsusAI/finbert')


# Checks if a Ticker is available via the Yahoo Finance API
def check_available(ticker: str) -> bool:
    info = yf.Ticker(ticker).history(period='1d', interval='1d')
    return len(info) > 0


def feed(ticker):
    rss_url = f'https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&lang=en-US'
    return feedparser.parse(rss_url)


def main():
    st.title('#📈 TICKER SENTIMENET ANALYZER')
    st.write('Enter a ticker and get the news sentiment for it.')

    total_score = 0
    num_articles = 0

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Prompts the user for a ticker input to get sentiment analysis
    if prompt_input := st.chat_input("Input Ticker, Filter (Example: META, Facebook)"):
        
        #######
        ### NEED TO ADD DEFESNE HERE
        #######
        prompt, filter = prompt_input.split(', ')

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt_input})
        with st.chat_message("user"):
            st.markdown(prompt_input)

        # Generate response using the rss feed if ticker is valid
        if check_available(prompt) == False:
            message = f'Sorry we were not able to find the ticker: {prompt}'
            st.session_state.messages.append({"role": "assistant", "content": message})
            with st.chat_message("assistant"):
                st.markdown(message)
        else:
            ticker_feed = feed(prompt)
            message = ''
            with st.chat_message("assistant"):
                st.markdown('-' * 40)
                
                for entries in ticker_feed.entries:
                    if filter.lower() not in entries.summary.lower():
                        continue
                    
                    sentiment =  classifier(entries.summary)[0]
                    
                    st.markdown(f'Title: {entries.title}')
                    st.markdown(f'Link: {entries.link}')
                    st.markdown(f'Published: {entries.published}')
                    st.markdown(f'Summary: {entries.summary}')
                    st.markdown(f'Sentiment: {sentiment["label"]}, Score: {sentiment["score"]}')
                    st.markdown('-' * 40)

                    if sentiment["label"] == 'positive' or sentiment["label"] == 'negative':
                        total_score += sentiment["score"]
                        num_articles += 1

                total = total_score / num_articles
                message = f'Overall Sentiment is {"Positive" if total >= 0.2 else "Negative" if total <= 0.2 else "Neutral"}: {total}'
                st.markdown(message)
                

if __name__ == '__main__':
    main()
