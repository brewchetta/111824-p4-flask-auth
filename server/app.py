#!/usr/bin/env python3

from flask import request, session
from models import db, User, Note
from config import app


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
        return new_user.to_dict(), 201
    except Exception as e:
        return { 'error': str(e) }, 400
    

# CHECK SESSION #

@app.get('/api/check_session')
def check_session():
    pass

# SESSION LOGIN/LOGOUT#

@app.post('/api/login')
def login():
    pass
    

@app.delete('/api/logout')
def logout():
    pass




# EXAMPLE OTHER RESOURCES #

@app.get('/api/notes')
def get_notes():
    all_notes = Note.query.all()
    return [note.to_dict() for note in all_notes], 200

@app.post('/api/notes')
def create_note():
    try:
        data = request.json
        new_note = Note(**data)
        db.session.add(new_note)
        db.session.commit()
        return new_note.to_dict(), 201
    except Exception as e:
        return {'error': str(e)}, 406

# APP RUN #

if __name__ == '__main__':
    app.run(port=5555, debug=True)
