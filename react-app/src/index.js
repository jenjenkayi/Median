import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import './index.css';
import App from './App';
import configureStore from './store';
import { ModalProvider, SelectedModals } from './context/Modal';
import { ModalProvider2, SelectedModals2 } from './context/Modal2';
import { BrowserRouter } from 'react-router-dom';

const store = configureStore();


function Root() {
  return (
    <Provider store={store}>
      <ModalProvider2>
        <ModalProvider>
          <SelectedModals />
          <SelectedModals2 />
          <BrowserRouter>
            <App />
          </BrowserRouter>
        </ModalProvider>
      </ModalProvider2>
    </Provider>
  )
}



ReactDOM.render(
  <React.StrictMode>
    <Root />
  </React.StrictMode>,
  document.getElementById('root')
);
