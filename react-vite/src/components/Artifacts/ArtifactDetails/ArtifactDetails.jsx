import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimes } from '@fortawesome/free-solid-svg-icons';
import { useParams, useNavigate } from "react-router-dom";
import { getTranscriptions, updateTranscription, deleteTranscription } from "../../../redux/transcriptions"; 
import './ArtifactDetails.css'

export default function ArtifactDetails() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { id } = useParams();
  const userId = useSelector((state) => state.session.user.id);
  const transcriptions = useSelector((state) => state.transcription.transcriptions);
  const [data, setData] = useState(null);
  const [text, setText] = useState(null);
  const [title, setTitle] = useState(null);
  const [editMode, setEditMode] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      await dispatch(getTranscriptions());
      const foundData = transcriptions.find((item) => item.id === Number(id)) || null;
      setData(foundData);
      setTitle(foundData.title);
      setText(foundData.text)
    };
    if (!data) {  
      fetchData();
    }
  }, [dispatch, id, transcriptions]);

  function handleSubmit() {
    dispatch(updateTranscription(id, text, title));
    navigate('/profile');
  }

  function handleDelete() {
    dispatch(deleteTranscription(id))
  }

  if (!data) return null; 

  const viewMode = 
    <div className="ArtifactDetails-div">
      <div className="ArtifactDetails-div-card">
        <h3 className="ArtifactDetails-title">{data.title}</h3>
        <div className="ArtifactDetails-div-infoBar">
        <ul className="ArtifactDetails-ul">
          <li className="ArtifactDetails-li">References</li>
          {(data.user_id === userId) &&
            <li className="ArtifactDetails-li" onClick={() => setEditMode(true)}>Edit</li>}
        </ul>
        </div>
        <p className="ArtifactDetails-transcription">{data.text}</p>
      </div>
    </div>;

  const editingMode = 
    <div className="ArtifactDetails-div">
      <div className="ArtifactDetails-div-card">
        <input type="text" value={title} className="ArtifactDetails-input-title" onChange={(e) => setTitle(e.target.value)}/>
        <div className="ArtifactDetails-div-infoBar">
        <ul className="ArtifactDetails-ul">
          <li className="ArtifactDetails-li" onClick={() => setEditMode(false)}>Exit</li>
          <li className="ArtifactDetails-li" onClick={() => handleSubmit()}>Save</li>
          <li className="ArtifactDetails-li" onClick={() => handleDelete()}>Delete</li>
        </ul>
        </div>
        <textarea value={text} className="ArtifactDetails-textarea-transcription" 
                  style={{height: `${Math.floor(text.length / 79) * 20 + 40}px`}} onChange={(e) => setText(e.target.value)}/>
      </div>
    </div>;

  return editMode ? editingMode : viewMode
}