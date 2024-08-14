#!/usr/bin/env python3

from flask import request, session
from models import db, User, Note
from config import app


URL_PREFIX = '/api'


# USER SIGNUP #

# @app.post(URL_PREFIX + '/users') OR
@app.post('/api/users')
def create_user():
    data = request.json
    try:
        new_user = User(username=data['username'])
        new_user.password = data['password']
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id # SETTING THE COOKIE
        return new_user.to_dict(), 201
    except Exception as e:
        return { 'error': str(e) }, 406
    

# CHECK SESSION #

@app.get('/api/check_session')
def check_session():
    user_id = session.get('user_id') # GET INFO FROM THE COOKIE
    if user_id:
        user = User.query.where(User.id == user_id).first()
        return user.to_dict(), 200
    else:
        return {}, 204

# SESSION LOGIN/LOGOUT#

@app.post('/api/login')
def login():
    data = request.json # { 'username': 'Chett', 'password': '123' }
    user = User.query.where(User.username == data['username']).first()
    if user and user.authenticate(data['password']):
        session['user_id'] = user.id # SETTING THE COOKIE
        return user.to_dict(), 201
    else:
        return { 'error': 'Invalid username or password' }, 401
    

@app.delete('/api/logout')
def logout():
    session.pop('user_id')
    return {}, 204




# EXAMPLE OTHER RESOURCES #

@app.get(URL_PREFIX + '/notes')
def get_notes():
    all_notes = Note.query.where(Note.user_id == session['user_id']).all()
    return [note.to_dict() for note in all_notes], 200

@app.post(URL_PREFIX + '/notes')
def create_note():
    try:
        data = request.json
        new_note = Note(**data)
        new_note.user_id = session['user_id']
        db.session.add(new_note)
        db.session.commit()
        return new_note.to_dict(), 201
    except Exception as e:
        return {'error': str(e)}, 406

# APP RUN #

if __name__ == '__main__':
    app.run(port=5555, debug=True)
