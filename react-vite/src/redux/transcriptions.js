const SET_TRANSCRIPTIONS = 'transcriptions/set_transcriptions'
const DELETE_TRANSCRIPTION = 'transcriptions/delete_transcriptions'

const setTranscriptions = (data) => ({
  type: SET_TRANSCRIPTIONS,
  payload: data
})

const removeTranscription = (id) => ({
  type: DELETE_TRANSCRIPTION,
  payload: id
})

export const getTranscriptions = () => async (dispatch) => {
  const response = await fetch('/api/transcription/');
  if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}
		dispatch(setTranscriptions(data));
	}
};

export const createTranscription = (text, title) => async (dispatch) => {
  const response = await fetch('/api/transcription/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      text: text,
      title: title,
    })
  })

  if (response.ok) {
    const data = await response.json()
  }
}

export const updateTranscription = (id, text, title) => async (dispatch) => {
  const response = await fetch(`/api/transcription/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ 
      text: text,
      title: title,
    })
  });
};

export const deleteTranscription = (id) => async (dispatch) => {
  const response = await fetch(`/api/transcription/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    }
  })

  if (response.ok) {
    dispatch(dele)
  }
};

const initialState = {};

export default function transcriptionReducer(state = initialState, action) {
  switch (action.type) {
    case SET_TRANSCRIPTIONS:
      return {...state, transcriptions: action.payload};
    case DELETE_TRANSCRIPTION:{
      let newState = {...state}
      delete newState.transcription.trasncriptions[action.payload]
      return newState
    }
    default: 
      return state;
  }
}