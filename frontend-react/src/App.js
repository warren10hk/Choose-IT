import React, { Component } from 'react';
import NavBar from './Common/NavBar';
import TypeButton from './Phone/TypeButton';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <NavBar></NavBar>
        <TypeButton></TypeButton>
      </div>
    );
  }
}

export default App;
