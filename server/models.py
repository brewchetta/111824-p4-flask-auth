### we'll use these later... ###
# bcrypt.generate_password_hash(password).decode('utf-8')
# bcrypt.check_password_hash(hashed_password, password)
#################################


from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt

# --- USERS --- #

class User(db.Model, SerializerMixin):

    __tablename__ = 'users_table'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String)

    notes = db.relationship('Note', back_populates='user')

    serialize_rules = ("-notes", "-password_hash")

    @property
    def password(self): # we will not let users see their password
        raise Exception("You may not see the password MWAHAHAHAHAHA")
    
    @password.setter
    def password(self, value): # ...but they can set their encrypted password
        self.password_hash = bcrypt.generate_password_hash(value).decode('utf-8')

    def authenticate(self, password_to_check): # ...and we can see if a password matches theirs
        return bcrypt.check_password_hash(self.password_hash, password_to_check) # True / False



# --- NOTES --- #

class Note(db.Model, SerializerMixin):

    __tablename__ = 'notes_table'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'), nullable=False)

    user = db.relationship('User', back_populates='notes')

    serialize_rules = ("-user.notes",)