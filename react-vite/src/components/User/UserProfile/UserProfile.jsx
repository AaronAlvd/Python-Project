import './UserProfile.css';
import UserArtifacts from '../UserArtifacts/UserArtifacts';
import UserPrompts from '../UserPrompts/UserPrompts';
import { useState } from 'react'

export default function UserProfile() {
  const [activeSection, setActiveSection] = useState('Artifacts');

  return (
    <div>
      <div className='UserProfile-div-img'>
        <h1 className="UserProfile-img">Image Here</h1>
      </div>
      <div style={{display: 'flex', justifyContent: 'center', borderTop: "1px solid black", borderBottom: "1px solid black"}}>
        <div className='UserProfile-div-infoBar'>
          <p className={activeSection === 'Artifacts' ? 'UserProfile-p-infoBar-active' : 'UserProfile-p-infoBar'}
             onClick={() => setActiveSection('Artifacts')}>My Artifacts</p>
          <span style={{minWidth: 1, minHeight: 20, maxHeight: 20, backgroundColor: 'black'}}/>
          <p className={activeSection === 'Prompts' ? 'UserProfile-p-infoBar-active' : 'UserProfile-p-infoBar'}
             onClick={() => setActiveSection('Prompts')}>My Prompts</p>
          <span style={{minWidth: 1, minHeight: 20, maxHeight: 20, backgroundColor: 'black'}}/>
          <p className={activeSection === 'References' ? 'UserProfile-p-infoBar-active' : 'UserProfile-p-infoBar'}
             onClick={() => setActiveSection('References')}>My References</p>
        </div>
      </div>
    </div>
  )
}