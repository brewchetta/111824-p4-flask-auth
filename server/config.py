import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()

# APP CONFIGURATION

app = Flask(__name__)
# THIS IS IMPORTANT FOR SECURITY!!! KEEP IT SAFE!!!
app.secret_key = os.environ.get('FLASK_SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

print( os.environ.get('FLASK_SECRET') )

CORS(app)

# DB CONFIGURATION

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

migrate = Migrate(app, db)

db.init_app(app)

# BCRYPT --- encryption tool for our passwords
bcrypt = Bcrypt(app)