from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# --- USERS --- #

class User(db.Model, SerializerMixin):

    __tablename__ = 'users_table'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _hashed_password = db.Column(db.String)

    notes = db.relationship('Note', back_populates='user')

    serialize_rules = ("-notes",)














# --- NOTES --- #

class Note(db.Model, SerializerMixin):

    __tablename__ = 'notes_table'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'), nullable=False)

    user = db.relationship('User', back_populates='notes')

    serialize_rules = ("-user.notes",)