import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getArticles } from '../../../redux/articles';
import './ArticlePage.css'


export default function ArticlePage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const articles = useSelector((state) => state.article.articles);
  const user = useSelector((state) => state.session.user)


  useEffect(() => {
    dispatch(getArticles())
  }, [dispatch])

  if (!articles) return null

  return (
    <div className='ArticlePage-div'>
      {articles.map((data) => {
        return (
          <div className='ArticlePage-div-card' onClick={() => navigate(`/articles/${data.slug || data.id}`)}>
            <p className='ArticlePage-text'>{data.text}</p>
          </div>
        )
      })}
    </div>
  )
}