import requests

def emotion_detector(text_to_analyse: str):
    "Executes Emotion Predict function of the  Watson NLP Library"

    req_data = {
            "url": 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
            "headers": {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
            "json": { "raw_document": { "text": text_to_analyse }},
    }

    res = requests.post(**req_data)
    print(res)



