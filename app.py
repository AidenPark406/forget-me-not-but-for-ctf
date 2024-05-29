from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_numbers', methods=['GET'])
def generate_numbers():
    numbers = [random.randint(0, 9) for _ in range(100)]
    return jsonify(numbers=numbers)

@app.route('/submit_numbers', methods=['POST'])
def submit_numbers():
    user_numbers = request.form.getlist('numbers[]')
    # For now, we'll just return the user's input
    return jsonify(user_numbers=user_numbers)

if __name__ == '__main__':
    app.run(debug=True)
