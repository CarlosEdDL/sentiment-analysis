from flask import Flask, jsonify, render_template, request
from sentiment import result_index


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict-sentiment', methods=['POST'])
def predict_sentiment():
    data = request.get_json()
    text = data['text']
    current_sentiment = result_index(text)
    return jsonify({'sentiment':current_sentiment})


if __name__ == "__main__":
    app.run(debug=True)
