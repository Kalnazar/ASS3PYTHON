from flask import *
import datetime
from flask_sqlalchemy import SQLAlchemy
import jwt
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:9803@localhost:5432/pythonAss3'
app.config['SECRET_KEY'] = 'thisismysecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class AllUsers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), nullable=False,unique=True)
    password = db.Column(db.String(255), nullable=False)
    token = db.Column(db.Text, nullable=False, default='')


@app.route('/')
@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    user = AllUsers.query.filter_by(login=auth.username).first()
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    if auth and auth.password == user.password:
        token = jwt.encode({'username': user.login, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)}, app.config['SECRET_KEY'])
        user = AllUsers.query.filter_by(login=auth.username).first()
        user.token = token
        db.session.commit()
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return '<h1>Hello, token is missing </h1>', 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return '<h1>Hello, Could not verify the token</h1>', 403

        return f(*args, **kwargs)

    return decorated


@app.route('/protected')
@token_required
def protected():
    return '<h1>Hello, token which is provided is correct</h1>'


if __name__ == '__main__':
    app.run(debug=True)


