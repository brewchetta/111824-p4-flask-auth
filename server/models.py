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

    serialize_rules = ("-notes.user", "-password_hash")

    @property
    def password(self):
        raise Exception('You may not see a user password')
    
    @password.setter
    def password(self, new_password):
        pw_hash = bcrypt.generate_password_hash(new_password).decode('utf-8')
        self.password_hash = pw_hash

    # rehashes and compares the new password and old password
    def authenticate(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

# --- NOTES --- #

class Note(db.Model, SerializerMixin):

    __tablename__ = 'notes_table'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'), nullable=False)

    user = db.relationship('User', back_populates='notes')

    serialize_rules = ("-user.notes",)