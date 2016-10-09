import React, { Component } from 'react';
import { Link } from 'react-router'

class Menu extends Component {
  render() {
    return (
      <ul className="mainMenu">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/about">About</Link></li>
      </ul>
    );
  }
}

export default Menu;
