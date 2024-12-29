import { getTranscriptions } from '../../../redux/transcriptions';
import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import './ArtifactPage.css'

export default function ArtifactPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [active, setActive] = useState(null)
  const transcriptions = useSelector((state) => state.transcription.transcriptions)

  useEffect(() => {
    dispatch(getTranscriptions())
  }, [dispatch]);

  return (
    <div className='ArtifactPage-div'>
      {transcriptions && transcriptions.map((data, index) => {
        return (
          <div style={{display: 'flex', justifyContent: 'center'}}>
            <div className='ArtifactPage-div-card' onClick={() => navigate(`/documents/${data.id}`)}>
              <div className='ArtifactPage-div-cardTitle'>
                <p className='ArtifactPage-title'>{data.title}</p>
              </div>
              <p className='ArtifactPage-p'>{data.text}</p>
            </div>
          </div>
        )
      })}
    </div>
  )
}