import { useState, useEffect } from 'react'
import NotesForm from './NotesForm'

function Notes() {

  // STATE //

  const [notes, setNotes] = useState([])

  useEffect(() => {
    fetch('/api/notes')
    .then(res => res.json())
    .then(data => setNotes(data))
  }, [])

  // EVENTS //

  function createNote(content) {
    fetch('/api/notes', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({content})
    })
    .then(res => {
      if (res.ok) {
        res.json()
        .then(newNote => setNotes([...notes, newNote]))
      } else {
        res.json()
        .then(data => alert(data.error))
      }
    })
  }

  // RENDER //

  return (

    <div>

      { notes.map(note => <h3>{note.id} {note.content}</h3>) }

      <NotesForm createNote={createNote} />

    </div>

  )

}

export default Notes
