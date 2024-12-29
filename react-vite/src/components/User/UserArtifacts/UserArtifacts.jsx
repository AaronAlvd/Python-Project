import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getTranscriptions } from '../../../redux/session';
import './UserArtifacts.css'

export default function UserArtifacts() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [active, setActive] = useState(null)
  const transcriptions = useSelector((state) => state.session.transcriptions)

  useEffect(() => {
    dispatch(getTranscriptions())
  }, [dispatch]);

  return (
    <div className='UserArtifacts-div'>
      {transcriptions && transcriptions.map((data, index) => {
        return (
          <div style={{display: 'flex', justifyContent: 'center'}}>
            <div className='UserArtifacts-div-card' onClick={() => navigate(`/documents/${data.id}`)}>
              <div className='UserArtifacts-div-cardTitle'>
                <p className='UserArtifacts-title'>{data.title}</p>
              </div>
              <p className='UserArtifacts-p'>{data.text}</p>
            </div>
          </div>
        )
      })}
    </div>
  )
}