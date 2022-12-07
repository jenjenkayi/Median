import { BrowserRouter } from "react-router-dom";
import { csrfFetch } from "./csrf";

// constants
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";

const setUser = (user) => ({
  type: SET_USER,
  payload: user,
});

const removeUser = () => ({
  type: REMOVE_USER,
});

export const authenticate = () => async (dispatch) => {
  const response = await csrfFetch("/api/auth/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }

    dispatch(setUser(data));
  }
};

export const login = (email, password) => async (dispatch) => {
  const response = await csrfFetch("/api/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });

  if (response.ok) {
    const data = await response.json();
    localStorage.setItem("logged", "true")
    dispatch(setUser(data));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};

export const logout = () => async (dispatch) => {
  const response = await csrfFetch("/api/auth/logout", {
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    localStorage.removeItem("logged")
    dispatch(removeUser());
  }
};

export const signUp =
(username, email, password, first_name, last_name) => async (dispatch) => {
  const response = await fetch("/api/auth/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      email,
      password,
      first_name,
      last_name,
    }),
  });

  if (response.ok) {
    localStorage.setItem("logged", "true")
    const data = await response.json();
    dispatch(setUser(data));
    return null;
  } else if (response.status < 500) {
      throw response;
    } else {
      return ["An error occurred. Please try again."];
    }
  };

const initialState = { user: null };

export function sessionReducer(state = initialState, action) {
  let newState;
  switch (action.type) {
    case SET_USER:
      newState = {...state, user: {...state.user}}
      // newState = Object.assign({}, state);
      newState.user = action.payload;
      return newState;
    case REMOVE_USER:
      newState = Object.assign({}, state);
      newState.user = null;
      return newState;
    default:
      return state;
  }
}
