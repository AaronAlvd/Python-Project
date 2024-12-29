import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getArticles, deleteArticle, updateArticle } from '../../../redux/articles';
import './ArticleDetails.css';

export default function ArticleDetails() {
  const { id, slug } = useParams();  // Extracting both id and slug
  const identifier = slug || id;
  const user = useSelector((state) => state.session.user)
  const dispatch = useDispatch();
  const articles = useSelector((state) => state.article.articles);
  const [data, setData] = useState()
  const [editMode, setEditMode] = useState(false)
  const [text, setText] = useState()
  const [format, setFormat] = useState()
  const [title, setTitle] = useState()

  useEffect(() => {
    const fetch = async () => {
      await dispatch(getArticles())
      const newData = articles.find((conn) => conn.slug === identifier || conn.id === Number(identifier))
      setData(newData)
      setFormat(newData.text.split('\n').filter((str) => str.length > 5))
      setText(newData.text)
      setTitle(newData.text.split('\n')[0])
    }

    if (!data || !articles) {
      fetch()
    }
  }, [dispatch, articles, title, identifier])

  function handleUpdate() {
    dispatch(updateArticle(id, text))
  }

  function handleDelete() {
    dispatch(deleteArticle(data.id))
  }

  function handleFormat() {
    return (
      <>
      <h4 style={{margin: '20px 0 5px 0'}}>{format[0]}</h4>
      <p className='ArticleDetails-text'>{format[1]}</p>

      <h4 style={{margin: '20px 0 5px 0'}}>{format[2]}</h4>
      <p className='ArticleDetails-text'>{format[3]}</p>
      <p className='ArticleDetails-text'>{format[4]}</p>

      <h4 style={{margin: '20px 0 5px 0'}}>{format[5]}</h4>
      <p className='ArticleDetails-text'>{format[6]}</p>
      <p className='ArticleDetails-text'>{format[7]}</p>

      <h4 style={{margin: '20px 0 5px 0'}}>{format[8]}</h4>
      <p className='ArticleDetails-text'>{format[9]}</p>
      <p className='ArticleDetails-text'>{format[10]}</p>

      <h4 style={{margin: '20px 0 5px 0'}}>{format[11]}</h4>
      <p className='ArticleDetails-text'>{format[12]}</p>
      <p className='ArticleDetails-text'>{format[13]}</p>

      <h4 style={{margin: '20px 0 5px 0'}}>{format[14]}</h4>
      <p className='ArticleDetails-text'>{format[15]}</p>
      <p className='ArticleDetails-text'>{format[16]}</p>
      </>
    )
  }

  if (!data || !articles || !title) return null

  const viewMode = (
    <div className='ArticleDetails-div'>
      <div className='ArticleDetails-div-card'>
        <div className='ArticleDetails-div-header'>
          <h3 className='ArticleDetails-title'>{data.title}</h3>
          <small>{user.first_name} {user.last_name}</small>
        </div>
        <div className="ArticleDetails-div-infoBar">
          <ul className="ArticleDetails-ul">
            <li className="ArticleDetails-li">References</li>
            {(data.user_id === user.id) &&
            <li className="ArticleDetails-li" onClick={() => setEditMode(true)}>Edit</li>}
          </ul>
        </div>
        {handleFormat()}
      </div>
    </div>
  )

  const editingMode = (
    <div className='ArticleDetails-div'>
      <div className='ArticleDetails-div-card'>
        <div className="ArticleDetails-div-infoBar">
          <ul className="ArticleDetails-ul">
            <li className="ArticleDetails-li" onClick={() => setEditMode(false)}>Exit</li>
            <li className="ArticleDetails-li" onClick={() => handleUpdate()}>Save</li>
            <li className="ArticleDetails-li" onClick={() => handleDelete()}>Delete</li>
          </ul>
        </div>
        <textarea value={text} onChange={(e) => setText(e.target.value)} className="ArticleDetails-textarea"
                  style={{height: `${Math.floor(text.length / 79) * 20 + 40}px`}}/>
      </div>
    </div>
  )

  return editMode ? editingMode : viewMode
}