#!/usr/bin/env python3

from flask import request, session
from models import db, User, Note
from config import app


# USER SIGNUP #

@app.post('/api/users')
def create_user():
    data = request.json
    try:
        new_user = User(username=data['username'])
        new_user.password = data['password']
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        return new_user.to_dict(), 201
    except Exception as e:
        return { 'error': str(e) }, 400
    

# CHECK SESSION #

@app.get('/api/check_session')
def check_session():
    user_id = session.get('user_id')
    user = User.query.where(User.id == user_id).first()
    if user:
        return user.to_dict(), 200
    else:
        return {}, 204

# SESSION LOGIN/LOGOUT#

@app.post('/api/login')
def login():
    data = request.json
    user = User.query.where(User.username == data.get('username')).first()
    if user and user.authenticate( data.get('password') ):
        session['user_id'] = user.id
        return user.to_dict(), 202
    else:
        return { 'error': 'Invalid username or password' }, 401
    

@app.delete('/api/logout')
def logout():
    session.pop('user_id')
    return {}, 204




# EXAMPLE OTHER RESOURCES #

@app.get('/api/notes')
def get_notes():
    user_id = session.get('user_id')
    all_notes = Note.query.where(Note.user_id == user_id).all()
    return [note.to_dict() for note in all_notes], 200

@app.post('/api/notes')
def create_note():
    try:
        data = request.json
        new_note = Note(content=data.get('content'))
        new_note.user_id = session.get('user_id')
        db.session.add(new_note)
        db.session.commit()
        return new_note.to_dict(), 201
    except Exception as e:
        return {'error': str(e)}, 406

# APP RUN #

if __name__ == '__main__':
    app.run(port=5555, debug=True)
