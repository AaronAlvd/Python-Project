import { useDispatch, useSelector } from 'react-redux';
import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { getSearchResults } from '../../redux/search';
import DocumentResults from './DocumentResults/DocumentResults';
import PromptResults from './PromptResults/PromptResults';
import './SearchResults.css'

export default function SearchResults() {
  const { query } = useParams();
  const results = useSelector((state) => state.search.searchResults )
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [active, setActive] = useState('documents');
  
  useEffect(() => {
    dispatch(getSearchResults(query))
  }, [dispatch])

  if (!results) return null;
  
  const displayArticles = () => {
    const data = results.articles;
    if (data.length === 0) return null;
    const retArr = new Array(data.length);
    for (let i = 0; i < data.length; i++) {
      const data2 = data[i]
      retArr[i] = 
        <div className='SearchResults-div-card'>
          <p className='SearchResults-title'>{data2.title}</p>
          <p className='SearchResults-text'>{data2.text}</p>
        </div> 
    }
    console.log(retArr)
    return retArr;
  }

  return (
    <div className='SearchResults-div'>
      <div className='SearchResults-titleSection'>
        <div className='SearchResults-titleBox' onClick={() => setActive('articles')}>
          <p className={(active === 'articles') ? 'SearchResults-title SearchResults-titleActive' : 'SearchResults-title'}>Articles</p>
        </div>
        <div className='SearchResults-titleBox' onClick={() => setActive('documents')}>
          <p className={(active === 'documents') ? 'SearchResults-title SearchResults-titleActive' : 'SearchResults-title'}>Documents</p>
        </div>
        <div className='SearchResults-titleBox' onClick={() => setActive('prompts')}>
          <p className={(active === 'prompts') ? 'SearchResults-title SearchResults-titleActive' : 'SearchResults-title'}>Prompts</p>
        </div>
      </div>
      {(active === 'documents') && <DocumentResults data={results.transcriptions}/>}
      {(active === 'prompt') && <PromptResults data={results.prompts}/>}
    </div>
  )
}