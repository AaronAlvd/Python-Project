const GET_SEARCH_RESULTS = 'search/getResults';

const setResults = (data) => ({
  type: GET_SEARCH_RESULTS,
  payload: data
})

export const getSearchResults = (query) => async (dispatch) => {
  const response = await fetch(`/api/searchEngine/${query}`)
  if (response.ok) {
    const data = await response.json()
    if (data.errors) {
      return;
    }
    dispatch(setResults(data))
  }
}

const initialState = {};

export default function searchReducer(state = initialState, action) {
  switch(action.type) {
    case GET_SEARCH_RESULTS:
      return { ...state, searchResults: action.payload}
    default:
      return state
  }
}