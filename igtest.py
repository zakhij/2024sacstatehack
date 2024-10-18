import openai
import base64
import os

openai.api_key = "KEY"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def get_travel_recommendations(image_paths) -> str:
    # Prepare the messages with all images
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Analyze these travel photos and provide a detailed description of the user's travel preferences based on what you see."}
            ] + [   
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encode_image(path)}"}} for path in image_paths
            ]
        }
    ]

    # Get the analysis response
    analysis_response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )

    new_input = analysis_response.choices[0].message.content

    # Prepare a new message for travel recommendations based on the analysis
    recommendation_message = [      
        {
            "role": "system",
            "content": "You are a travel expert. Based on the analysis of the user's travel preferences, provide personalized travel recommendations."
        },
        {
            "role": "user",
            "content": f"Based on this analysis of my travel preferences, can you suggest some travel destinations and activities that I might enjoy?\n\nAnalysis: {new_input}"
        }
    ]   

    # Get travel recommendations
    recommendation_response = openai.chat.completions.create(
        model="gpt-4",
        messages=recommendation_message,
    )

    return recommendation_response.choices[0].message.content







