import { useDispatch, useSelector } from "react-redux";
import { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import { getPrompts } from '../../../redux/session';
import './UserPrompts.css'

export default function UserPrompts() {
  const dispatch = useDispatch();
  const prompts = useSelector((state) => state.session.prompts);
  const navigate = useNavigate();

  useEffect(() => {
    dispatch(getPrompts())
  }, [dispatch]);

  return (
    <div className="UserPrompts-div">
      {prompts && prompts.map((data, index) => {
       return (
        <div className="UserPrompts-div-card" onClick={() => navigate(`/prompts/${data.id}`)}>
          <p className="UserPrompts-prompt">{data.prompt}</p>
        </div>
       )
      })}
    </div>
  )
}