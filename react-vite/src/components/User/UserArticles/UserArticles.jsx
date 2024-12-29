import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getArticles } from '../../../redux/session';
import './UserArticles.css'


export default function UserArticles() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const articles = useSelector((state) => state.session.articles);
  const user = useSelector((state) => state.session.user)


  useEffect(() => {
    dispatch(getArticles())
  }, [dispatch])

  if (!articles) return null

  return (
    <div className='UserArticles-div'>
      {articles.map((data) => {
        return (
          <div className='UserArticles-div-card' onClick={() => navigate(`/articles/${data.slug || data.id}`)}>
            <p className='UserArticles-text'>{data.text}</p>
          </div>
        )
      })}
    </div>
  )
}