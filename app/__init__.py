from flask import Flask
from flask_mail import Mail



app = Flask(__name__)
app.config['SECRET_KEY'] = 'jeriaplace'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'd80abf79509b4d'
app.config['MAIL_PASSWORD'] = '3ae3137a767ecb'



mail = Mail(app)
from app import views

