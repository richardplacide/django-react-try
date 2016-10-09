import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import About from './pages/About.js';
import './index.css';
import { Router, Route, hashHistory } from 'react-router';

ReactDOM.render(
  <Router history={hashHistory}>
    <Route path="/" component={App}/>
    <Route path="/about" component={About}/>
  </Router>,
  document.getElementById('root')
);


/*

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
*/
