import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getPrompts, updatePrompts, deletePrompts } from '../../redux/prompts';
import './PromptDetails.css';

export default function PromptDetails() {
  const { id } = useParams();
  const dispatch = useDispatch();
  const userId = useSelector((state) => state.session.user.id);
  const prompts = useSelector((state) => state.prompt.prompts);
  const [data, setData] = useState();
  const [editMode, setEditMode] = useState(false);
  const [text, setText] = useState();

  useEffect(() => {
   const fetchData = async () => {
    await dispatch(getPrompts());
    const foundData = prompts.find(prompt => prompt.id === Number(id));
    setData(foundData);
    setText(foundData.prompt);
   }
   if (!data) {  
    fetchData();
   }
  }, [dispatch, prompts, id]);

  function handleSubmit() {
    dispatch(updatePrompts(id, text))
  };

  function handleDelete() {
    dispatch(deletePrompts(id))
  }

  const viewMode =
    (<div className='PromptDetails-div'>
      {data && 
      <div className='PromptDetails-div-card'>
        <div className="PromptDetails-div-infoBar">
        <ul className="PromptDetails-ul">
          <li className="PromptDetails-li">References</li>
          {(data.user_id === userId) &&
            <li className="PromptDetails-li" onClick={() => setEditMode(true)}>Edit</li>}
        </ul>
        </div>
        <p className='PromptDetails-prompt'>{data.prompt}</p>
      </div>}
    </div>);

  const editingMode =
    (<div className='PromptDetails-div'>
      {data && 
      <div className='PromptDetails-div-card'>
        <div className="PromptDetails-div-infoBar">
        <ul className="PromptDetails-ul">
          <li className="PromptDetails-li" onClick={() => setEditMode(false)}>Exit</li>
          <li className="PromptDetails-li" onClick={() => handleSubmit()}>Save</li>
          <li className="PromptDetails-li" onClick={() => handleDelete()}>Delete</li>
        </ul>
        </div>
        <textarea value={text} onChange={(e) => setText(e.target.value)} className='PromptDetails-textarea'
                  style={{height: `${Math.floor(text.length / 79) * 20 + 40}px`}}/>
      </div>}
    </div>);

  return editMode ? editingMode : viewMode
  
};