import { getTranscriptions } from '../../../redux/transcriptions';
import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import './UserArtifacts.css'

export default function UserArtifacts() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [active, setActive] = useState(null)
  const transcriptions = useSelector((state) => state.transcription.transcriptions)

  useEffect(() => {
    dispatch(getTranscriptions())
  }, [dispatch]);

  return (
    <div className='UserArtifacts-div'>
      {transcriptions && transcriptions.map((data, index) => {
        return (
          <div style={{display: 'flex', justifyContent: 'center'}}>
            <div className='UserArtifacts-div-card' onClick={() => navigate(`/transcription/${data.id}`)}>
              <div className='UserArtifacts-div-cardTitle'>
                <h4 className='UserArtifacts-h4'>{data.title}</h4>
              </div>
              <p className='UserArtifacts-p'>{data.text}</p>
            </div>
          </div>
        )
      })}
    </div>
  )
}