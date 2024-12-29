const GET_ARTICLES = 'article/get_articles';
const DELETE_ARTICLE = 'article/delete_article'

const setArticles = (data) => ({
  type: GET_ARTICLES,
  payload: data
});

const removeArticle = (id) => ({
  type: DELETE_ARTICLE,
  payload: id
})

export const getArticles = () => async (dispatch) => {
  const response = await fetch('/api/article/')
  if (response.ok) {
    const data = await response.json()
    if (data.errors) {
      return;
    }
    dispatch(setArticles(data))
  }
}

export const createArticle = (article, title, slug) => async (dispatch) => {
  const response = await fetch('/api/article/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      article: article,
      title: title,
      slug: slug
    })
  })

  if (response.ok) {
    const data = await response.json()
    return data;
  }
}

export const updateArticle = (id, article) => async (dispatch) => {
  const response = await fetch(`/api/article/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      article: article
    }),
  })
}

export const deleteArticle = (id) => async (dispatch) => {
  const response = await fetch(`/api/article/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    },
  })

  if (response.ok) {
    dispatch(removeArticle(id))
  }
}

const initialState = {}

export default function articleReducer(state = initialState, action) {
  switch (action.type) {
    case GET_ARTICLES:
      return {...state, articles: action.payload}
    case DELETE_ARTICLE: {
      let newState = {...state}
      delete newState.article.articles[action.payload]
      return newState
    }
    default:
      return state
  }
}

