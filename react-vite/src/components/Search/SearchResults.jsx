import { useDispatch, useSelector } from 'react-redux';
import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { getSearchResults } from '../../redux/search';
import './SearchResults.css'

export default function SearchResults() {
  const { query } = useParams();
  const results = useSelector((state) => state.search.searchResults )
  const navigate = useNavigate();
  const dispatch = useDispatch();
  
  useEffect(() => {
    dispatch(getSearchResults(query))
  }, [dispatch])

  if (!results) return null;

  const displayDocuments = () => {
    const data = results.transcriptions;
    if (data.length === 0) return null;
    const retArr = new Array(data.length);
    for (let i = 0; i < data.length; i++) {
      const data2 = data[i]
      retArr[i] = (
        <div className='SearchResults-div-card'>
          <p className='SearchResults-title'>{data2.title}</p>
          <p className='SearchResults-text'>{data2.text}</p>
        </div>
      )
    }
    return retArr;
  }
  
  const displayArticles = () => {
    const data = results.articles;
    if (data.length === 0) return null;
    const retArr = new Array(data.length);
    for (let i = 0; i < data.length; i++) {
      const data2 = data[i]
      retArr[i] = (
        <div className='SearchResults-div-card'>
          <p className='SearchResults-title'>{data2.title}</p>
          <p className='SearchResults-text'>{data2.text}</p>
        </div>
      )
    }
    return retArr;
  }
  const displayPrompts = () => {
    const data = results.prompts;
    if (data.length === 0) return null;
    const retArr = new Array(data.length);
    for (let i = 0; i < data.length; i++) {
      const data2 = data[i]
      retArr[i] = (
        <div className='SearchResults-div-card'>
          <p className='SearchResults-title'>{data2.title}</p>
          <p className='SearchResults-text'>{data2.prompt}</p>
        </div>
      )
    }
    return retArr;
  }

  const className = () => {
    const len1 = results.transcriptions.length; 
    const len2 = results.articles.length; 
    const len3 = results.prompts.length;
    
    if (len1 && len2 && len3) return 'SearchResults-div-3'
    else if ((len1 || len2) && (len2 || len3)) return 'SearchResults-div-2'
    else return 'SearchResults-div'
  }

  return (
    <div className={className()}>
      {displayArticles() ? 
      <div>
        <h3 style={{margin: '0 0 10px 0'}}>Articles</h3>
        {displayArticles()}
      </div> : null}

      {displayDocuments() ? 
      <div>
        <h3 style={{margin: '0 0 10px 0'}}>Documents</h3>
        {displayDocuments()}
      </div> : null}

      {displayPrompts() ? 
      <div>
        <h3> style={{margin: '0 0 10px 0'}}Prompts</h3>
        {displayPrompts()}
      </div> : null}
    </div>
  )
}