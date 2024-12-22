
const GET_PROMPTS = 'prompts/getPrompts'
const DELETE_PROMPT = 'prompts/deletePrompts'

const setPrompts = (data) => ({
  type: GET_PROMPTS,
  payload: data
});

const removePrompts = (id) => ({
  type: DELETE_PROMPT,
  payload: id
})

export const getPrompts = () => async (dispatch) => {
  const response = await fetch('/api/prompt/');
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return
    }
    dispatch(setPrompts(data));
  }
};

export const createPrompt = (prompt) => async (dispatch) => {
  const response = await fetch('/api/prompt/', {
    method: 'CREATE',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      prompt: prompt
    })
  })

}

export const updatePrompts = (id, prompt) => async (dispatch) => {
  const response = await fetch(`/api/prompt/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      prompt: prompt
    }),
  })
};

export const deletePrompts = (id) => async (dispatch) => {
  const response = await fetch(`/api/prompt/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    }
  })

  if (response.ok) {
    dispatch(removePrompts(id))
  }
};

const initialState = {};

export default function promptReducer(state = initialState, action) {
  switch(action.type) {
    case GET_PROMPTS: 
      return {...state, prompts: action.payload}
    case DELETE_PROMPT: {
      let newState = {...state}
      delete newState.prompt.prompts[action.payload]
      return newState
    }
    default:
      return state
  }
};