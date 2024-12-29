import './ArtifactForm.css'
import { useState, useEffect } from 'react'
import { createTranscription } from '../../../redux/transcriptions'
import { useDispatch } from 'react-redux'

export default function ArtifactForm() {
  const [title, setTitle] = useState()
  const [text, setText] = useState()
  const dispatch = useDispatch()

  async function handleSubmit(e) {
    e.preventDefault();

    // Check if title or text are empty
    if (!title || !text) {
        console.log("Title and text are required");
        return;  // Early return to stop the function
    }

    try {
        // Dispatch action to create transcription
        await dispatch(createTranscription(text, title));

        // Optionally clear the input fields after successful submission
        setTitle('');
        setText('');
    } catch (error) {
        console.error("Error submitting transcription:", error);
        // Handle error if needed, such as showing a message to the user
    }
  }

  return (
    <div className='ArtifactForm-div'>
      <form className='ArtifactForm-form'>
        <div className='ArtifactForm-div-input' style={{display: 'flex'}}>
          <input type="text" className='ArtifactForm-input' value={title} onChange={(e) => setTitle(e.target.value)}/>
          <span className='ArtifactForm-span-label'>
            <button className='ArtifactForm-button' onClick={(e) => handleSubmit(e)}>Create</button>
          </span>
        </div>

        <div className='ArtifactForm-div-textarea'>
          <textarea className='ArtifactForm-textarea' value={text} onChange={(e) => setText(e.target.value)}/>
        </div>
      </form>
    </div>
  )
}