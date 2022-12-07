import { csrfFetch } from "./csrf";
const LOAD_ALL_STORIES = "/stories/LOAD_ALL_STORIES";
const LOAD_USERS_STORIES = "/stories/LOAD_USERS_STORIES";
const LOAD_SINGLE_STORIES = "/stories/LOAD_SINGLE_STORIES";
const NEW_STORY = "/stories/NEW_STORY";
const EDIT_STORY = "/stories/EDIT_STORY";
const DESTORY_STORY = "/stories/DESTORY_STORY";

// ACTIONS
const allStories = (stories) => {
  return {
    type: LOAD_ALL_STORIES,
    stories,
  };
};

const usersStories = (stories) => {
  return {
    type: LOAD_USERS_STORIES,
    stories,
  };
};

const singleStory = (story) => {
  return {
    type: LOAD_SINGLE_STORIES,
    story,
  };
};

const newStory = (story) => {
  return {
    type: NEW_STORY,
    story,
  };
};

const editStory = (story) => {
  return {
    type: EDIT_STORY,
    story,
  };
};

const destroyStory = (storyId) => {
  return {
    type: DESTORY_STORY,
    storyId,
  };
};

// THUNKS

// Get All Stories
export const getAllStories = () => async (dispatch) => {
  const res = await csrfFetch("/api/stories");
  if (res.ok) {
    const stories = await res.json();
    dispatch(allStories(stories));
    return stories;
  }
};

// Get all Stories by a UserId
export const getUsersStories = (userId) => async (dispatch) => {
  const res = await csrfFetch(`/api/users/${userId}/stories`);
  if (res.ok) {
    const stories = await res.json();
    dispatch(usersStories(stories));
    return stories;
  }
};

// Get details of a Story from an id
export const getSingleStory = (storyId) => async (dispatch) => {
  const res = await csrfFetch(`/api/stories/${storyId}`);
  if (res.ok) {
    const story = await res.json();
    dispatch(singleStory(story));
    return story;
  }
};

// Create a Story
export const createStory = (data) => async (dispatch) => {
  const res = await csrfFetch("/api/stories/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  if (res.ok) {
    const story = res.json();
    dispatch(newStory(story));
    return story;
  }
};

export const updateStory = (storyId, data) => async (dispatch) => {
  const res = await csrfFetch(`/api/stories/${storyId}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (res.ok) {
    const story = res.json();
    dispatch(editStory(story));
    return story;
  }
};

export const deleteStory = (storyId) => async (dispatch) => {
  const res = await csrfFetch(`/api/stories/${storyId}`, {
    method: "DELETE",
  });
  if (res.ok) {
    dispatch(destroyStory(storyId));
  }
};

export const addLikeToStory = (storyId, count) => async (dispatch) => {
  const resp = await csrfFetch(`/api/stories/${storyId}/likes`, {
    method: "POST",
    body: JSON.stringify({ count: count }),
  });
  if (resp.ok) {
    return;
  }
};

let initialState = {
  allStories: {},
  singleStory: {},
};

export const storyReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD_ALL_STORIES:
      const allStories = { ...state, allStories: {} };
      action.stories.Stories.forEach((ele) => {
        allStories.allStories[ele.id] = ele;
      });
      return allStories;
    case LOAD_USERS_STORIES:
      const usersStories = { ...state, allStories: {} };
      action.stories.Stories.forEach((ele) => {
        usersStories.allStories[ele.id] = ele;
      });
      return usersStories;
    case LOAD_SINGLE_STORIES:
      const singleStory = { ...state, singleStory: action.story };
      // singleStory.singleStory = action.story;
      return { ...singleStory };
    case NEW_STORY:
      const newStory = { ...state, singleStory: {} };
      newStory.singleStory = action.story;
      return newStory;
    case EDIT_STORY:
      const editedStory = { ...state, singleStory: {} };
      editedStory.singleStory = action.story;
      return editedStory;
    case DESTORY_STORY:
      const deleteStory = {
        allStories: { ...state.allStories },
        singleStory: { ...state.singleStory },
      };
      deleteStory.singleStory = {};
      delete deleteStory.allStories[action.storyId];
      return { ...deleteStory };
    default:
      return state;
  }
};
