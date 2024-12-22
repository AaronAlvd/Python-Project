import './UserProfile.css';
import UserArtifacts from '../UserArtifacts/UserArtifacts';
import UserPrompts from '../UserPrompts/UserPrompts';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus, faPlusCircle, faPlusSquare } from '@fortawesome/free-solid-svg-icons';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function UserProfile() {
  const [activeSection, setActiveSection] = useState('Artifacts');
  const navigate = useNavigate();

  function handleClick() {
    if (activeSection === 'Artifacts') return navigate('/transcription/form')
    else if (activeSection === 'Prompts') return navigate('/prompt/form')
    else if (activeSection === 'Connections') return navigate('/connection/form')
  }

  return (
    <div>
      <div className='UserProfile-div-img'>
        <img className="UserProfile-img" src="/default_photo.webp"/>
      </div>
      <div style={{display: 'flex', justifyContent: 'center', borderTop: "1px solid black", borderBottom: "1px solid black"}}>
        <FontAwesomeIcon icon={faPlusSquare} className='UserProfile-icon' onClick={() => handleClick()}/>
        <div className='UserProfile-div-infoBar'>
          <p className={activeSection === 'Artifacts' ? 'UserProfile-p-infoBar-active' : 'UserProfile-p-infoBar'}
             onClick={() => setActiveSection('Artifacts')}>My Artifacts</p>
          <span style={{minWidth: 1, minHeight: 20, maxHeight: 20, backgroundColor: 'black'}}/>
          <p className={activeSection === 'Prompts' ? 'UserProfile-p-infoBar-active' : 'UserProfile-p-infoBar'}
             onClick={() => setActiveSection('Prompts')}>My Prompts</p>
          <span style={{minWidth: 1, minHeight: 20, maxHeight: 20, backgroundColor: 'black'}}/>
          <p className={activeSection === 'Connections' ? 'UserProfile-p-infoBar-active' : 'UserProfile-p-infoBar'}
             onClick={() => setActiveSection('Connections')}>Connections</p>
        </div>
      </div>
      {activeSection === 'Artifacts' && <UserArtifacts/>}
      {activeSection === 'Prompts' && <UserPrompts />}
      {activeSection === 'Connections' && <Connections />}
    </div>
  )
}
