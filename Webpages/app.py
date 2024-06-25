from flask import Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    hometown = db.Column(db.String(50), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_list = [{'name': user.name, 'email': user.email, 'phone': user.phone, 'dob': user.dob, 'hometown': user.hometown} for user in users]
    return jsonify({'users': users_list})

@app.route('/data', methods=['POST'])
def create_user():
    if not request.form or not 'name' in request.form:
        abort(400, 'Name is required')
    user = User(
        name=request.form['name'],
        email=request.form.get('email', ''),
        phone=request.form.get('phone', ''),
        dob=request.form.get('dob', ''),
        hometown=request.form.get('hometown', '')
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Data submitted successfully', 'user': {'name': user.name, 'email': user.email, 'phone': user.phone, 'dob': user.dob, 'hometown': user.hometown}}), 201

@app.route('/show-users')
def show_users():
    users = User.query.all()
    return render_template('show_users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
