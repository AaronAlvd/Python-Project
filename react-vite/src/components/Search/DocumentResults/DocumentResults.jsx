import './DocumentResults.css';

export default function DocumentResults({ data }) {

  const displayDocuments = () => {
    if (data.length === 0) return null;
    const retArr = new Array(data.length);
    for (let i = 0; i < data.length; i++) {
      const data2 = data[i]
      retArr[i] = 
        <div className='DocumentResults-card'>
          <p className='DocumentResults-title'>{data2.title}</p>
          <p className='DocumentResults-text'>{data2.text}</p>
        </div>
    }
    return retArr;
  }

  if (!data) return null;

  return (
    <div className='DocumentResults-grid'>
      {displayDocuments()}
    </div>
  )
}