import { useDispatch, useSelector } from 'react-redux';
import { useState } from 'react';
import { createPrompt } from '../../../redux/prompts';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faExclamationTriangle } from '@fortawesome/free-solid-svg-icons';
import './PromptForm.css';


export default function PromptForm() {
  const dispatch = useDispatch()
  const [text, setText] = useState()
  const [displayError, setDisplayError] = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()

    if (!text) {
      setDisplayError(true)
      return null
    }

    const response = await dispatch(createPrompt(text))
    console.log(JSON.stringify(response))
  }

  return(
    <div className='PromptForm-div'>
      <form className='PromptForm-form'>
        <div className='PromptForm-div-title' style={{display: 'flex'}}>
          <p className='PromptForm-title'>Prompt</p>
          <span className='PromptForm-span-label'>
            <button className='PromptForm-button' onClick={(e) => handleSubmit(e)}>Create</button>
          </span>
        </div>

        <div className='PromptForm-div-textarea'>
          <textarea className='PromptForm-textarea' value={text} onChange={(e) => setText(e.target.value)}/>
        </div>
      </form>
      {displayError && 
      <div className='PromptForm-div-error'>
        <p className='PromptForm-error'>text is required <FontAwesomeIcon icon={faExclamationTriangle}/></p>
      </div>}
    </div>
  )
}