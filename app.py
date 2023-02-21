from flask import Flask,render_template,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from datetime import datetime
import cloudinary
import cloudinary.uploader
import cloudinary.api
import base64


from dotenv import load_dotenv
load_dotenv()


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///user.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.config['SECRET_KEY']='this_is_the_secret_key'
db=SQLAlchemy(app)

config = cloudinary.config(secure=True)



class User(db.Model):
    __tablename__ = 'user'
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    invitation_code=db.Column(db.String(100),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)->str:
        return f"{self.sno}-{self.email}"
    
app.app_context().push()
db.create_all()

@app.route('/start_test',methods=["GET"])
def start_test():
    return render_template('index.html')


@app.route('/start_test',methods=["POST"])
def start_test_1():
    if request.method=="POST":
        print(request)
        name=request.form['name']
        email=request.form['email']
        invitation_code=request.form['invitation_code']
        user=User.query.filter_by(email=email).first()
        print(user)
        if user==None:
            user=User(name=name,email=email,invitation_code=invitation_code)
            db.session.add(user)
            db.session.commit()
            return redirect('/test')
        else:
            print("A user with this email already exists")
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template("test.html")


@app.route('/image', methods=['POST'])
def image():

    data = request.get_json()

    imageURL = data.get('image', None)

    if (imageURL is None):
        return {}, 400


    print(imageURL)

    now=datetime.now()
    date_time = now.strftime("%m-%d-%Y-%H-%M-%S")

    cloudinary.uploader.upload(file=imageURL, folder=f"images", public_id=date_time, overwrite=True)
   
    return {},200

if __name__=='__main__':
    app.run(debug=True)


