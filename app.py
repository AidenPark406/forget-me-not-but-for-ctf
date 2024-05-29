from flask import Flask, render_template, jsonify, request, session, flash, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    flag_message = session.pop('flag_message', None)  # Retrieve the flag message from the session if available
    return render_template('index.html', flag_message=flag_message)

@app.route('/generate_numbers', methods=['GET'])
def generate_numbers():
    numbers = [random.randint(1, 9) for _ in range(96)]
    session['numbers'] = numbers  # Store the numbers in the session for later validation
    expected_presses = " ".join("".join(map(str, numbers[i:i+3])) for i in range(0, len(numbers), 3))
    print(f"Expected button presses for each stage: {expected_presses}")
    return jsonify(numbers=numbers)

@app.route('/submit_number', methods=['POST'])
def submit_number():
    user_number = request.form.get('number')
    stage = int(request.form.get('stage'))
    correct_number = session['numbers'][stage]
    
    if user_number == str(correct_number):
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route('/submit_numbers', methods=['POST'])
def submit_numbers():
    user_numbers = request.form.getlist('numbers[]')
    if len(user_numbers) == 96 and all(user_numbers[i] == str(session['numbers'][i]) for i in range(96)):
        flash('btctf{example_flag_here}')
        session['flag_message'] = 'btctf{example_flag_here}'
    return jsonify(user_numbers=user_numbers)

if __name__ == '__main__':
    app.run(debug=True)
