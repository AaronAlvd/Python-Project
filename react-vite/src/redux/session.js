const SET_USER = 'session/setUser';
const REMOVE_USER = 'session/removeUser';
const SET_TRANSCRIPTIONS = 'transcriptions/set_transcriptions';
const GET_PROMPTS = 'prompts/getPrompts';
const GET_ARTICLES = 'article/get_articles';

const setUser = (user) => ({
  type: SET_USER,
  payload: user
});

const setTranscriptions = (data) => ({
  type: SET_TRANSCRIPTIONS,
  payload: data
})

const setArticles = (data) => ({
  type: GET_ARTICLES,
  payload: data
});

const setPrompts = (data) => ({
  type: GET_PROMPTS,
  payload: data
});

const removeUser = () => ({
  type: REMOVE_USER
});

export const thunkAuthenticate = () => async (dispatch) => {
	const response = await fetch("/api/auth/");
	if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}

		dispatch(setUser(data));
	}
};

export const getPrompts = () => async (dispatch) => {
  const response = await fetch('/api/user/prompt');
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return
    }
    dispatch(setPrompts(data));
  }
};

export const getTranscriptions = () => async (dispatch) => {
  const response = await fetch('/api/user/transcription');
  if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}
		dispatch(setTranscriptions(data));
	}
};

export const getArticles = () => async (dispatch) => {
  const response = await fetch('/api/user/article')
  if (response.ok) {
    const data = await response.json()
    if (data.errors) {
      return;
    }
    dispatch(setArticles(data))
  }
}

export const thunkLogin = (credentials) => async dispatch => {
  const response = await fetch("/api/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials)
  });

  if(response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
  } else if (response.status < 500) {
    const errorMessages = await response.json();
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
};

export const thunkSignup = (user) => async (dispatch) => {
  const response = await fetch("/api/auth/signup", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(user)
  });

  if(response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
  } else if (response.status < 500) {
    const errorMessages = await response.json();
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
};

export const thunkLogout = () => async (dispatch) => {
  await fetch("/api/auth/logout");
  dispatch(removeUser());
};

const initialState = { 
  user: null, 
  transcriptions: null,
  articles: null,
  prompts: null,
};

function sessionReducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { ...state, user: action.payload };
    case SET_TRANSCRIPTIONS:
      return {...state, transcriptions: action.payload };
    case GET_PROMPTS:
      return {...state, prompts: action.payload}
    case GET_ARTICLES:
      return {...state, articles: action.payload}
    case REMOVE_USER:
      return { ...state, user: null };
    default:
      return state;
  }
}

export default sessionReducer;
