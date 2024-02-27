import base64
import requests
import os
from IPython.display import Image, display
import sys



GPT4V_KEY = "ab4b9c5540a54a549331f4249e5f2070"
GPT4V_ENDPOINT = "https://openai4gpt98.openai.azure.com/openai/deployments/gptdemo/extensions/chat/completions?api-version=2023-07-01-preview"



img_path = "images/kill.jpg"

display(Image(img_path))


def image_gpt4v(query):

    # Configuration
    IMAGE_PATH = img_path
    encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
    headers = {
        "Content-Type": "application/json",
        "api-key": GPT4V_KEY,
    }

    # Payload for the request
    payload = {
      "enhancements": {
        "ocr": {
          "enabled": True
        },
        "grounding": {
          "enabled": True
        }
      },
      "messages": [
        {
          "role": "system",
          "content": [
            {
              "type": "text",
              "text": "You are an AI assistant that helps people find information."
            }
          ]
        },
        {
          "role": "user",
          "content": [
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{encoded_image}"
              }
            },
            {
              "type": "text",
              "text": query
            }
          ]
        }
      ],
      "temperature": 0.7,
      "top_p": 0.95,
      "max_tokens": 800
    }
    # Send request
    try:
        response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

    # Handle the response as needed (e.g., print or process)
    return response.json()['choices'][0]['message']['content']



i = 0

while i < 10:
    query = input("Enter your query :")
    print(image_gpt4v(query))
    i += 1