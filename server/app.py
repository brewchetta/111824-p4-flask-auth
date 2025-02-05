#!/usr/bin/env python3

from flask import request, session
from models import db, User, Note
from config import app

# USER SIGNUP #

@app.post('/api/users')
def create_user():
    try:
        body = request.json
        new_user = User(**body)
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        return new_user.to_dict(), 201
    except:
        return { 'error': "Generic error here" }, 400

# CHECK SESSION #

@app.get('/api/check_session')
def check_session():
    user = User.query.where(User.id == session.get('user_id')).first()
    if user:
        return user.to_dict(), 200
    else:
        return {}, 204

# SESSION LOGIN/LOGOUT#

@app.post('/api/login')
def login():
    body = request.json
    user = User.query.where(User.username == body.get('username')).first()
    if user and user.authenticate( body.get('password') ):
        session['user_id'] = user.id
        return user.to_dict(), 201
    else:
        return { 'error': 'Invalid username or password' }, 401

@app.delete('/api/logout')
def logout():
    session.pop('user_id')
    return {}, 204



# EXAMPLE OTHER RESOURCES #

@app.get('/api/notes')
def get_notes():
    # we only get the notes for the logged in user
    all_notes = Note.query.where(Note.user_id == session.get('user_id')).all()
    return [note.to_dict() for note in all_notes], 200

@app.post('/api/notes')
def create_note():
    try:
        body = request.json
        # we automatically assign notes to the logged in user
        new_note = Note(content=body.get('content'), user_id=session.get('user_id'))
        db.session.add(new_note)
        db.session.commit()
        return new_note.to_dict(), 201
    except Exception as e:
        return {'error': str(e)}, 406

# APP RUN #

if __name__ == '__main__':
    app.run(port=5555, debug=True)
