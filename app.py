from flask import Flask, render_template, request
from utils.model import predict_career

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    skills = request.form.get('skills')
    interests = request.form.get('interests')

    
    user_input = skills + " " + interests

    career, score = predict_career(user_input)

    return render_template('index.html',
                           career=career,
                           score=round(score * 100, 2))


if __name__ == '__main__':
    app.run(debug=True)
