from flask import Flask,redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/DummyApi"
app.config['SECRET_KEY'] = "Iambishnudevkhutia0"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if(db):
    print("Connected to DB successfully")
else:
    print("Error! Could not connect to DB")

class API(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    roll = db.Column(db.String(50),nullable = False)
    lang = db.Column(db.String(50),nullable = False)

@app.route('/')
def helloWorld():
    return 'Hello,World!'

@app.route('/api-list',methods = ['GET'])
def apis():
    if request.method == 'GET':
        allApi = API.query.all()
    return allApi

@app.route('/post-api',methods = ['POST'])
def postApi():
    if request.method == 'POST':
        name = request.json
        roll = request.json
        lang = request.json
        if(name, roll, lang):
            storeData = API(name = name, roll = roll, lang = lang)
            db.session.add(storeData)
            db.session.commit()
            return redirect('/api-list')
    return "New api added!"

@app.route('/delete-api/<int:id>')
def deleteApi(id):
    api = API.query.filter_by(id=id).first()
    db.session.delete(api)
    db.session.commit()
    return redirect('/api-list')


@app.route('/update-api/<int:id>')
def updateApi(id):
    newname = request.json
    newroll = request.json
    newlang = request.json
    if(newlang,newname,newroll):
        api = API.query.filter_by(id=id).first()
        api.name = newname
        api.roll = newroll
        api.lang = newlang
        db.session.add(api)
        db.session.commit()
        return redirect('/api-list')
    return 'Api updated!'


if __name__ == "__main__":
    app.run(debug = True)