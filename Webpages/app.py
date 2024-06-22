from flask import Flask, render_template, request, jsonify, abort

app = Flask(__name__)

# Data storage (simulating a database)
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_all_users():
    return jsonify({'users': users})

@app.route('/data', methods=['POST'])
def create_user():
    if not request.form or not 'name' in request.form:
        abort(400, 'Name is required')
    user = {
        'name': request.form['name'],
        'email': request.form.get('email', ''),
        'phone': request.form.get('phone', ''),
        'dob': request.form.get('dob', ''),
        'hometown': request.form.get('hometown', '')
    }
    users.append(user)
    return jsonify({'message': 'Data submitted successfully', 'user': user}), 201

if __name__ == '__main__':
    app.run(debug=True)