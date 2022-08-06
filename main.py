import email
from flask import Flask, render_template, request, flash 
from form import ContactForm
import json
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine
import requests
from flask import * 
from flask_mail import * 



app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com' 
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME'] = 'sbnamratha08@gmail.com' 
app.config['MAIL_PASSWORD'] = 'odkymnqwooenlkkd' 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True 
mail = Mail(app)
 
app.config['MONGODB_SETTINGS'] = {
 'db': 'R',
'host': 'localhost',
'port': 27017
}
db = MongoEngine()
db.init_app(app)
app.secret_key = 'development key'

@app.route('/')
def index():
      return render_template('index.html')

class Rf(db.Document):
     name = db.StringField()
     usn = db.StringField()
     email=db.StringField()
     branch=db.StringField()
     year=db.StringField()
     college=db.StringField()
     def to_json(self):
         return {"name": self.name,
                  "usn": self.usn,
                  "email":self.email,
                  "branch":self.branch,
                  "year":self.year,
                  "college":self.college
                  } 
 

@app.route('/', methods=['POST'])
def create_record():
 
 record = json.loads(request.data)
 c = Rf(name=record['name'],
            usn=record['usn'],
            email=record['email'],
            branch=record['branch'],
            year=record['year'],
            college=record['college']
            )
 c.save()
 return jsonify(c.to_json())


@app.route('/add',methods=['GET','POST'])
def add():
 form = ContactForm()  
 if request.method=="GET":
   return render_template("contact.html",form=form)
 else:
      x={
   "name":request.form['name'],
   "usn":request.form['usn'],
   "email":request.form['email'],
   "branch":request.form['branch'],
   "year":request.form['year'],
   "college":request.form['college']
   }
      msg = Message('subject', sender = 'sbnamratha08@gmail.com',recipients=[request.form["email"]]) 
      msg.body = "name :"+str(request.form['name'])+"\n"+"USN :"+request.form['usn']+"\n"+request.form['email']+"\n"+"Branch :"+request.form['branch']+"\n"+"Year"+request.form['year']+"\n"+"College :"+request.form['college']
      mail.send(msg)
      y=json.dumps(x)
    
      response = requests.post(url="http://127.0.0.1:5000/",data=y)
      #loaded_json = json.loads(x)
      
      return render_template('x.html',a=x)
 
if __name__ == '__main__': 
 app.run(debug = True)