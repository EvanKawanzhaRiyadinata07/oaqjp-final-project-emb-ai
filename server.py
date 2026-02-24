from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    text_to_analyze = request.form['text']
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Teks tidak valid! Silakan coba lagi."

    response = f"Untuk teks yang diberikan, sistem merespon dengan 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}. Emosi dominannya adalah <b>{result['dominant_emotion']}</b>."
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)