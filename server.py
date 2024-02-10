from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    req = request.args.get("text_to_analyse")
    res = emotion_detector(req)
    
    
    if res["dominant_emotion"] is None:
        return "Invalid Text! Please try again"
    
    return f"""
For the given statement, the system response is 'anger': {res["anger"]},
 'disgust': {res["disgust"]}, 'fear': {res["fear"]}, 'joy': {res['joy']} and
 'sadness': {res["sadness"]}. The dominant emotion is {res["dominant_emotion"]}
            """

@app.route("/")
def home():
    return render_template("./templates/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    
