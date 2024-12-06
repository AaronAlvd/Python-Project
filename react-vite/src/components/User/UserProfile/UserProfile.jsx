import './UserProfile.css';
import UserArtifacts from '../UserArtifacts/UserArtifacts';
import UserPrompts from '../UserPrompts';

export default function UserProfile() {


  return (
    <div>
      <h1 className="UserProfile-img">Image Here</h1>
      <div className='UserProfile-div-infoBar'>
        <h3 className='UserProfile-h3-infoBar'>My Artifacts</h3>
        <span style={{minWidth: 2, minHeight: 25, maxHeight: 25, backgroundColor: 'black'}}/>
        <h3 className='UserProfile-h3-infoBar'>My Prompts</h3>
        <span style={{minWidth: 2, minHeight: 25, maxHeight: 25, backgroundColor: 'black'}}/>
        <h3 className='UserProfile-h3-infoBar'>My References</h3>
      </div>
    </div>
  )
}