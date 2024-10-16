import streamlit as st
import requests

def generate_tweet(prompt, gemini_api_key):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gemini_api_key}"
    }
    data = {
        "prompt": f"Generate a tweet based on the prompt: \"{prompt}\"",
        "temperature": 0.7,  # Adjust temperature for creativity vs. formality
        "max_tokens": 150,  # Adjust maximum token length
        "n": 1  # Generate one tweet
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return "Error generating tweet."

def main():
    st.title("Tweet Generator")

    prompt = st.text_input("Enter your tweet prompt:")
    gemini_api_key = st.text_input("Enter your Gemini API key:")

    if st.button("Generate Tweet"):
        if not gemini_api_key:
            st.warning("Please enter your Gemini API key.")
        else:
            generated_tweet = generate_tweet(prompt, gemini_api_key)
            st.text_area("Generated Tweet:", value=generated_tweet, height=200)

if __name__ == "__main__":
    main()
