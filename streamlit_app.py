import streamlit as st
import requests
from PIL import Image

def generate_tweet(prompt, image_url, gemini_api_key):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gemini_api_key}"
    }
    data = {
        "prompt": f"Generate a tweet based on the prompt: \"{prompt}\". Include a relevant image link: \"{image_url}\".",
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
    image_upload = st.file_uploader("Upload an image (optional):")
    gemini_api_key = st.text_input("Enter your Gemini API key:")

    if st.button("Generate Tweet"):
        if not gemini_api_key:
            st.warning("Please enter your Gemini API key.")
        elif image_upload:
            image = Image.open(image_upload)
            st.image(image)
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Tux.png/220px-Tux.png"  # Replace with actual image URL
            generated_tweet = generate_tweet(prompt, image_url, gemini_api_key)
        else:
            generated_tweet = generate_tweet(prompt, None, gemini_api_key)

        st.text_area("Generated Tweet:", value=generated_tweet, height=200)

if __name__ == "__main__":
    main()
