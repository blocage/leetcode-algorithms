import React from "react";
import Destination from './destination.jsx';

export default class WelcomePage extends React.Component {
  render() {
    return (
      <div className='container'>
        <h1>Welcome to homegame</h1>
        <h2>Choose your destination:</h2>
        <div className='media-list'>

          <Destination description='Leetcode'
                      href='#/galaxy/leetcode?cx=-2273&cy=93&cz=2677&lx=-0.0206&ly=-0.3646&lz=-0.0009&lw=0.9309&ml=150&s=1.75&l=1&v=2015-09-27T13-00-00Z'
                      media='composer_fly_first.png'
                      name='Leetcode solutions'/>
        </div>
      </div>
    );
  }
}
