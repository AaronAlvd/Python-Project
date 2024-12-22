const GET_CONNECTIONS = 'connection/get_connections';
const DELETE_CONNECTION = 'connection/delete_connection'

const setConnections = (data) => ({
  type: GET_CONNECTIONS,
  payload: data
});

const removeConnection = (id) => ({
  type: DELETE_CONNECTION,
  payload: id
})

export const getConnection = () => async (dispatch) => {
  const response = await fetch('/api/connection/')
  if (response.ok) {
    const data = await response.json()
    if (data.errors) {
      return;
    }
    dispatch(setConnections(data))
  }
}

export const createConnection = (connection) => async (dispatch) => {
  const response = await fetch('/api/connection/', {
    method: 'CREATE',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      connection: connection
    })
  })
}

export const updateConnection = (id, connection) => async (dispatch) => {
  const response = await fetch(`/api/connection/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      connection: connection
    }),
  })
}

export const deleteConnection = (id) => async (dispatch) => {
  const response = await fetch(`/api/connection/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    },
  })

  if (response.ok) {
    dispatch(removeConnection(id))
  }
}

const initialState = {}

export default function connectionReducer(state = initialState, action) {
  switch (action.type) {
    case GET_CONNECTIONS:
      return {...state, connections: action.payload}
    case DELETE_CONNECTION: {
      let newState = {...state}
      delete newState.connection.connections[action.payload]
      return newState
    }
    default:
      return state
  }
}

