import React from 'react';
import './Footer.css';
import { Button } from './Button';

function Footer() {
  return (
    <div className='footer-container'>
      <section className='footer-subscription'>
        <p className='footer-subscription-heading'>
          Join the Community to Save the Planet
        </p>
        <p className='footer-subscription-text'>
          You can unsubscribe at any time.
        </p>
        <div className='input-areas'>
          <form>
            <input
              className='footer-input'
              name='email'
              type='email'
              placeholder='Your Email'
            />
            <Button buttonStyle='btn--outline'>Subscribe</Button>
          </form>
        </div>
      </section>
      <div className='footer-links'>
        <div className='footer-link-wrapper'>
          <div className='footer-link-items'>
            <h2>About Us</h2>
          </div>
          <div className='footer-link-items'>
            <h2>Contact Us</h2>
          </div>
          <div className='footer-link-items'>
            <h2>Social Media</h2>
          </div>
        </div>
      </div>
      <section className='social-media'>
        <div className='social-media-wrap'>
          <small className='website-rights'>Endangered Animals © 2024</small>
          <div className='social-icons'>
            <a
              className='social-icon-link facebook'
              href='https://www.facebook.com'
              target='_blank'
              rel='noopener noreferrer'
              aria-label='Facebook'
            >
              <i className="fa-brands fa-facebook"/>
            </a>
            <a
              className='social-icon-link instagram'
              href='https://www.instagram.com'
              target='_blank'
              rel='noopener noreferrer'
              aria-label='Instagram'
            >
              <i className='fa-brands fa-instagram'/>
            </a>
            <a
              className='social-icon-link linkedin'
              href='https://www.linkedin.com'
              target='_blank'
              rel='noopener noreferrer'
              aria-label='LinkedIn'
            >
              <i className='fa-brands fa-linkedin' />
            </a>
            <a
              className='social-icon-link discord'
              href='https://www.discord.com'
              target='_blank'
              rel='noopener noreferrer'
              aria-label='Discord'
            >
              <i className='fa-brands fa-discord' />
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Footer;
