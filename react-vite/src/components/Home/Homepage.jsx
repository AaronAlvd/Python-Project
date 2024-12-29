import './Homepage.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch, faGlobe, faFileAlt, faPen } from '@fortawesome/free-solid-svg-icons';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { getSearchResults } from '../../redux/search';
import { useEffect, useState } from 'react';

export default function Homepage() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [query, setQuery] = useState();

  return (
    <div className='Homepage-div'>
      <div style={{height: 50}}/>

      <div style={{display: 'flex', margin: '20px'}}>
        <div className='Homepage-div-searchBar'>
          <input type='text' value={query} className='Homepage-input' placeholder='search...' onChange={(e) => setQuery(e.target.value)}/>
        </div>
        <div className='Homepage-div-searchIcon'>
          <FontAwesomeIcon icon={faSearch} onClick={() => navigate(`/searchEngine/${query}`)}/>
        </div>
      </div>

      <div style={{height: 50}}/>

      <div className='Homepage-div-body'>
          <div className="Homepage-div-col1">
            <FontAwesomeIcon icon={faGlobe} style={{fontSize: 60, cursor: 'pointer'}} onClick={() => navigate('/articles/all')}/>
            <div className='Homepage-div-box' onClick={() => navigate('/articles/all')}>
              <h1 className='Homepage-h1'>Articles</h1>
              <p className='Homepage-p'>
                The Articles section is where transformed and reimagined content comes to life. Users can take a document and select a prompt from 
                the Prompts section to rewrite the original material into a new format. Whether it’s turning a historical document into a news 
                article or reformatting it into a fictional narrative, this section showcases the results of blending original content with 
                creative direction.
              </p>
            </div>
          </div>
          <div className="Homepage-div-col2">
            <FontAwesomeIcon icon={faFileAlt} style={{fontSize: 60, cursor: 'pointer'}} onClick={() => navigate('/documents/all')}/>
            <div className='Homepage-div-box' onClick={() => navigate('/documents/all')}>
              <h1 className='Homepage-h1'>Documents</h1>
              <p className='Homepage-p'>
                The Documents section serves as a repository for text transcriptions of real-world documents. These documents can include 
                historical texts, official records, or any written material that has been digitized for ease of access and use. It provides a 
                foundational resource for users to reference or work with as part of the creative or analytical process.
              </p>
            </div>
          </div>
          <div className="Homepage-div-col3">
            <FontAwesomeIcon icon={faPen} style={{fontSize: 60, cursor: 'pointer'}} onClick={() => navigate('/prompts/all')}/>
            <div className='Homepage-div-box' onClick={() => navigate('/prompts/all')}>
              <h1 className='Homepage-h1'>Prompts</h1>
              <p className='Homepage-p'>
                The Prompts section houses a curated collection of writing prompts designed to inspire creativity or guide the transcription and 
                reformatting of content. These prompts can range from formal styles, such as academic or legal formats, to more creative ones 
                like storytelling or journalistic approaches. They act as templates or starting points for transforming documents into new forms.
              </p>
            </div>
          </div>
      </div>
    </div>
  )
}