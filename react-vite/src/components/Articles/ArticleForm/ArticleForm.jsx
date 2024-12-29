import { useDispatch, useSelector } from 'react-redux';
import { useState } from 'react';
import { createArticle } from '../../../redux/articles';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faExclamationTriangle } from '@fortawesome/free-solid-svg-icons';
import './ArticleForm.css';


export default function ArticleForm() {
  const dispatch = useDispatch()
  const [text, setText] = useState()
  const [title, setTitle] = useState()
  const [slug, setSlug] = useState()
  const [displayError, setDisplayError] = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()

    if (!text || !title || !slug ) {
      setDisplayError(true)
      return null
    }

    const response = await dispatch(createArticle(text, title, slug))
    console.log(JSON.stringify(response))
  }

  return(
    <div className='ArticleForm-div'>
      <form className='ArticleForm-form'>
        <div className='ArticleForm-div-slug'>
          <small className='ArticleForm-small'>localhost:5183/article/</small>
          <input type='text' className='ArticleForm-input-slug' value={slug} onChange={(e) => setSlug(e.target.value)}/>
          <span className='ArticleForm-span-slug'>
            <label className='ArticleForm-label-slug'>Slug</label>
          </span>
        </div>
        <div className='ArticleForm-div-title' style={{display: 'flex'}}>
          <input type="text" className='ArticleForm-input-title' value={title} onChange={(e) => setTitle(e.target.value)}/>
          <span className='ArticleForm-span-label'>
            <label className='ArticleForm-label'>Title</label>
          </span>
        </div>

        <div className='ArticleForm-div-textarea'>
          <textarea className='ArticleForm-textarea' value={text} onChange={(e) => setText(e.target.value)}/>
        </div>
        <button onClick={(e) => handleSubmit(e)}>Submit</button>
      </form>
      {displayError && 
      <div className='ArticleForm-div-error'>
        <p className='ArticleForm-error'>text is required <FontAwesomeIcon icon={faExclamationTriangle}/></p>
      </div>}
    </div>
  )
}