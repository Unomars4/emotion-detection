import requests

def emotion_detector(text_to_analyse: str):
    "Executes Emotion Predict function of the  Watson NLP Library"

    req_data = {
            "url": 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
            "headers": {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
            "json": { "raw_document": { "text": text_to_analyse }},
    }
    res = None
    
    if res.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None} 
    
    res = requests.post(**req_data)
    
    emotion_responses = res.json()["emotionPredictions"][0]["emotion"]
    highest_emotion_response = max((emotion_responses[emot], emot) for emot in emotion_responses)
    return {**emotion_responses, "dominant_emotion": highest_emotion_response[1]}
