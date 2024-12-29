import { useDispatch, useSelector } from "react-redux";
import { getPrompts } from '../../../redux/prompts';
import { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import './PromptPage.css'

export default function PromptPage() {
  const dispatch = useDispatch();
  const prompts = useSelector((state) => state.prompt.prompts);
  const navigate = useNavigate();

  useEffect(() => {
    dispatch(getPrompts())
  }, [dispatch]);

  return (
    <div className="PromptPage-div">
      {prompts && prompts.map((data, index) => {
       return (
        <div className="PromptPage-div-card" onClick={() => navigate(`/prompts/${data.id}`)}>
          <p className="PromptPage-prompt">{data.prompt}</p>
        </div>
       )
      })}
    </div>
  )
}