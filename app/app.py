from flask import Flask, render_template, request, url_for, redirect, session
import pandas as pd
from flask_session import Session
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from oauth.db_functions import update_or_create_user
import os
import logging
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, text 

load_dotenv() 

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/app.log",
    filemode="w",
    format='%(levelname)s - %(name)s - %(message)s'
)

app = Flask(__name__)

app.secret_key = os.urandom(12)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
oauth = OAuth(app)

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))


# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
)
engine = create_engine(conn_string, echo=False)

## Connection settings for the Goolge OAuth
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

@app.route("/")
def index():
    try:
        logging.debug("You have successfully accessed the index page!")
        return render_template('index.html')
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return "Please try again!"

@app.route('/login/')
def google():
    return render_template('google_login.html')

@app.route('/login/google/')
def login():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    print('REDIRECT URL: ', redirect_uri)
    session['nonce'] = generate_token()
    redirect_uri = 'https://5000-cs-174475239264-default.cs-us-east1-vpcf.cloudshell.dev/google/auth/'
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')
    
@app.route('/data')
def hospital_reports():
    with engine.connect() as connection:
        query4 = text('SELECT * FROM hospital_reports')
        result4 = connection.execute(query4)
        db_data4 = result4.fetchall()
    return render_template('hospital_reports.html', data4=db_data4)
    
@app.route('/patients')
def patients():
    with engine.connect() as connection:
        query1 = text('SELECT * FROM patients')
        result1 = connection.execute(query1)
        db = result1.fetchall()
        return render_template('patients.html', data1=db)

@app.route('/doctors')
def doctors():
    with engine.connect() as connection:
        query2 = text('SELECT * FROM doctors')
        result2 = connection.execute(query2)
        db_data2 = result2.fetchall()
    return render_template('doctors.html', data2=db_data2)

@app.route('/appointments')
def appointments():
    with engine.connect() as connection:
        query3 = text('SELECT * FROM appointments')
        result3 = connection.execute(query3)
        db_data3 = result3.fetchall()
    return render_template('appointments.html', data3=db_data3)

@app.route("/error")
def error():
    try:
        output = 1/0
        logging.debug("Success!!")
        return output
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return "Please Try Again!"

if __name__ == '__main__':
    app.run(debug=False, host = '0.0.0.0', port = 8080)

