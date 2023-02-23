from flask import Flask,render_template,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from datetime import datetime
import cloudinary
import cloudinary.uploader
import cloudinary.api
import base64
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors=CORS(app)
CORS(app, resources={r"/*": {"origins": "chrome-extension://jgenmihahfkpmbifjpdpoegjkijoahnf"}})

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
    email=db.Column(db.String(100),unique=True,nullable=False)
    invitation_code=db.Column(db.String(100),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
  
class Image(db.Model):
    __tablename__ = 'image'
    sno=db.Column(db.Integer,primary_key=True)
    id=db.Column(db.Integer,nullable=False)
    image=db.Column(db.String(10000),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)->str:
        return f"{self.sno}-{self.image}"
    
app.app_context().push()
db.create_all()





@app.route('/submit-data', methods=['POST'])
@cross_origin()
def submit_data():
  data = request.get_json()
  name = data['name']
  email = data['email']
  invitation_code = data['invitation_code']
  user=User(name=name,email=email,invitation_code=invitation_code)
  db.session.add(user)
  db.session.commit()
  response = ({'result': 'success'})
  return response

@app.route('/image', methods=['POST'])
@ cross_origin()
def image():

    data = request.get_json()

    imageURL = data.get('image', None)
    email=data.get('info',None)
    print(email)

    user=User.query.filter_by(email=email).first()
    print(user.sno)



    if (imageURL is None):
        return {}, 400

    image=Image(id=user.sno,image=imageURL)
    db.session.add(image)
    db.session.commit()

    print(imageURL)

    now=datetime.now()
    date_time = now.strftime("%m-%d-%Y-%H-%M-%S")

    cloudinary.uploader.upload(file=imageURL, folder=f"images/{user.sno}", public_id=date_time, overwrite=True)
   
    return {},200

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    alluser=User.query.all()
    print(alluser)
    return render_template('index.html',alluser=alluser)

@app.route('/user_image/<int:id>', methods=['GET'])
def user_image(id):
    image_list=list(Image.query.filter_by(id=id))
    return render_template("image.html",image_list=image_list)
    
    

if __name__=='__main__':
    app.run(debug=True)





















# @app.route('/start_test',methods=["GET"])
# @cross_origin()
# def start_test():
#     return render_template('index.html')


# @app.route('/start_test',methods=["POST"])
# @cross_origin()
# def start_test_1():
#     if request.method=="POST":
#         print(request)
#         name=request.form['name']
#         email=request.form['email']
#         invitation_code=request.form['invitation_code']
#         user=User.query.filter_by(email=email).first()
#         print(user)
#         if user==None:
#             user=User(name=name,email=email,invitation_code=invitation_code)
#             db.session.add(user)
#             db.session.commit()
#             return render_template('test.html')
#         else:
#             print("A user with this email already exists")
#     return render_template('index.html')


# @app.route('/test')
# @ cross_origin()
# def test():
#     return render_template("test.html")