"""
Flask web application for emotion detection
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Handle form submission and return emotion analysis"""
    # Get text from form
    text_to_analyze = request.form['text']
    
    # Check if input is empty
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid input! Try again."
    
    # Get emotion analysis
    result = emotion_detector(text_to_analyze)
    
    # Format the response
    if result['dominant_emotion']:
        response = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    else:
        response = "Invalid input! Try again."
    
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)