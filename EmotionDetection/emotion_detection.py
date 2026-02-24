"""
Module for emotion detection using Watson NLP API.
"""
import requests

def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using Watson NLP API.
    
    Parameters:
    text_to_analyse (str): Text to analyze for emotions
        
    Returns:
    dict: Dictionary containing emotion scores and dominant emotion
    """
    # URL endpoint for Watson NLP API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required by the API
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON format expected by the API
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    # Send POST request to the API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_dict = response.json()
        
        # Extract emotions from the response
        emotions = response_dict['emotionPredictions'][0]['emotion']
        
        # Format the output as required
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness']
        }
        
        # Find the dominant emotion (emotion with highest score)
        dominant_emotion = max(result, key=result.get)
        result['dominant_emotion'] = dominant_emotion
        
        return result
    else:
        # Return None values if request failed
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }