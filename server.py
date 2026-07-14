from flask import Flask, render_template, request
from emotion_detector import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    
    result = emotion_detector(text_to_analyze)
    
    # Check if result is None or dominant_emotion is None (blank/invalid entry)
    if result is None or result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400
    
    # Format the response as requested
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']
    
    response_text = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    
    return response_text

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
