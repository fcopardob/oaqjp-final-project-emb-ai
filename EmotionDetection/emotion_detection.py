import requests
import json

def emotion_detector(text_to_analyze):
    '''
    función que llama al analizador de emociones
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers = header)

    data = json.loads(response.text)

    if response.status_code == 200:

        emotions = data.get("emotionPredictions", [{}])[0].get("emotion", {})

        anger = emotions.get("anger")
        disgust = emotions.get("disgust")
        fear = emotions.get("fear")
        joy = emotions.get("joy")
        sadness = emotions.get("sadness")

        emotion_values = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }
        dominant = max(emotion_values, key=emotion_values.get)

    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant = None

    else:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant = None
    
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant}
