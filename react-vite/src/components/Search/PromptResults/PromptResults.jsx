import './PromptResults.css';

export default function PromptResults({ data }) {

  const displayPrompts = () => {
    if (data.length === 0) return null;
    const retArr = new Array(data.length);
    for (let i = 0; i < data.length; i++) {
      const data2 = data[i]
      retArr[i] = 
        <div className='PromptResults-card'>
          <p className='PromptResults-title'>{data2.title}</p>
          <p className='PromptResults-text'>{data2.prompt}</p>
        </div>
    }
    return retArr;
  }

  if (!data) return <h1>No Prompts Found</h1>

  return(
    <div className="PromptResults-grid">
      {displayPrompts()}
    </div>
  )
}