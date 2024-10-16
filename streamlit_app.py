import streamlit as st
import openai
import requests

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

# Set up Unsplash API key
UNSPLASH_ACCESS_KEY = "your_unsplash_access_key"

def generate_tweet(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Generate a tweet about {prompt}:",
        max_tokens=60
    )
    return response.choices[0].text.strip()

def search_images(query):
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)
    return response.json()['results']

st.title("Tweet Generator with Image Selection")

with st.sidebar:
    prompt = st.text_input("Enter a topic for your tweet:")
    if st.button("Generate Tweet"):
        tweet = generate_tweet(prompt)
        st.session_state.tweet = tweet

tab1, tab2 = st.tabs(["Generated Tweet", "Image Selection"])

with tab1:
    if 'tweet' in st.session_state:
        st.text_area("Generated Tweet", st.session_state.tweet, height=100)

with tab2:
    image_query = st.text_input("Search for images:")
    if st.button("Search Images"):
        images = search_images(image_query)
        cols = st.columns(3)
        for idx, image in enumerate(images[:9]):
            with cols[idx % 3]:
                st.image(image['urls']['small'], use_column_width=True)
                if st.button(f"Select Image {idx + 1}"):
                    st.session_state.selected_image = image['urls']['regular']

if 'tweet' in st.session_state and 'selected_image' in st.session_state:
    st.subheader("Preview")
    st.text_area("Final Tweet", st.session_state.tweet, height=100)
    st.image(st.session_state.selected_image, use_column_width=True)
