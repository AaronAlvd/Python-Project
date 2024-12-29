import './UserProfile.css';
import UserArtifacts from '../UserArtifacts/UserArtifacts';
import UserPrompts from '../UserPrompts/UserPrompts';
import UserArticles from '../UserArticles/UserArticles';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus, faPlusCircle, faPlusSquare } from '@fortawesome/free-solid-svg-icons';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';

export default function UserProfile() {
  const user = useSelector((state) => state.session.user)
  const [activeSection, setActiveSection] = useState('Artifacts');
  const navigate = useNavigate();

  function handleClick() {
    if (activeSection === 'Artifacts') return navigate('/documents/form')
    else if (activeSection === 'Prompts') return navigate('/prompts/form')
    else if (activeSection === 'Articles') return navigate('/articles/form')
  }

  if (!user) {
    return (
      <h2>Must Sign In</h2>
    )
  }

  return (
    <div>
      <div className='UserProfile-div-profile'>
        <h3 style={{margin: 20}}>{user.first_name} {user.last_name}</h3>
        <h4 style={{margin: 20}}>{user.email}</h4>
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
          <p className={activeSection === 'Articles' ? 'UserProfile-p-infoBar-active' : 'UserProfile-p-infoBar'}
             onClick={() => setActiveSection('Articles')}>Articles</p>
        </div>
      </div>
      {activeSection === 'Artifacts' && <UserArtifacts/>}
      {activeSection === 'Prompts' && <UserPrompts />}
      {activeSection === 'Articles' && <UserArticles />}
    </div>
  )
}
