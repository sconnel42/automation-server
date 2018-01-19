# A simple REST API that can run in the background. This is already on Nginx,
# and has its on systemd servicec, so you need to do to update it is run 
# `sudo systemctl restart automation-server`

from app_def import app, bcrypt, DBSession, request, jsonify
from flask import Response
from models import User

# Simple welcome page
@app.route("/", methods=['GET'])
def hello():
    return "<h1 style='color:green'>Hello There!</h1>"

@app.route("/login", methods=['POST'])
def login():
    is_valid = False
    username = request.get_json()["username"]
    password = request.get_json()["password"]

    user = DBSession.query(User).filter(User.name == username).first()
    if user:
        if bcrypt.check_password_hash(user.pw_hash, password):
            return Response("{'message':'Login successful!'}", status=200, mimetype='application/json')
        return Response("{'message':'Login failed!'}", status=401, mimetype='application/json')
    return Response("{'message':'No such user.'}", status=403, mimetype='application/json')

@app.route("/create_user", methods=['POST'])
def create_user():
    data = request.get_json()
    
    if data:
        try:
            username = data["username"]
            email = data['email']
            password = data["password"]
        except:
            return Response("{'message':'Bad data provided'}", status=403, mimetype='application/json')
    else:
        return Response("{'message':'No data provided'}", status=403, mimetype='application/json')

    user = DBSession.query(User).filter(User.name == username).first()
    if user:
        return Response("{'message':'User already exists!'}", status=403, mimetype='application/json')
    user = User(name=username, email=email, password=password)    
    DBSession.add(user)
    DBSession.flush()
    DBSession.commit()
    return Response("{'message':'User created successfully'}", status=201, mimetype='application/json')

# Running locally
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
