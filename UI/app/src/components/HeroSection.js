import React from 'react';
import { Button } from './Button';
import './HeroSection.css';
import '../App.css';

function HeroSection() {
  return (
    <div className='hero-container'>
      <video src="/videos/Giant_Panda.webm" autoPlay loop muted />
      <h1>Endangered Animals</h1>
      <p>Database and Model</p>
      <div className="hero-btns">
        <Button className='btns' buttonStyle='btn--outline' buttonSize='btn--large' to='/model'>
          Identify an Animal
        </Button>
      </div>
    </div>
  );
}

export default HeroSection;

