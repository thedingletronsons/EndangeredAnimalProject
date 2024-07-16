import React from 'react';
import './Cards.css';
import CardItem from './CardItem';

function Cards() {
  return (
    <div className='cards'>
      <h1>Check out these Endangered Animals!</h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <CardItem
              src='/images/Siberian_Tiger.jpg'
              text='Siberian Tiger'
              label='Photo by Dave Pape, public domain'
              path='/DataBase'
            />
          </ul>
          <ul className='cards__items'>
            <CardItem
              src='/images/African_Bush_Elephant.jpg'
              text='African Bush Elephant'
              label='Photo by Derek Keats, Creative Commons Attribution 2.0 License'
              path='/DataBase'
            />
            <CardItem
              src='/images/California_Condor.jpg'
              text='California Condor'
              label='Photo by USGov-FWS, public domain'
              path='/DataBase'
            />
          </ul>
          <ul className='cards__items'>
            <CardItem
              src='/images/Axolotl.jpg'
              text='Axolotl'
              label='Photo by Amandasofiarana, Creative Commons Attribution-Share Alike 4.0 License'
              path='/sign-up'
            />
            <CardItem
              src='/images/Green_Turtle.jpg'
              text='Green Turtle'
              label='Photo by Brocken Inaglory, Creative Commons Attribution-Share Alike 3.0 License'
              path='/sign-up'
            />
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;
