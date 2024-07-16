import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  const [click, setClick] = useState(false);
  const closeMobileMenu = () => setClick(false);
  const handleClick = () => setClick(!click);
  return (
    <>
    <nav className='navbar'>
        <div className='navbar-container'>
            <Link to="/" className="navbar-logo">
                ENAnimals <i className='fa-solid fa-otter'/>
            </Link>
            <div classname='menu-icon' onClick={handleClick}>
                <i className={click ? 'fas fa-times' : 'fas fa-bars'}/>
            </div>
            <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                <li className='nav-item'>
                    <Link to="/" className='nav-links' onClick={closeMobileMenu}>
                        Home
                    </Link>
                </li>
                <li className='nav-item'>
                    <Link to="/Database" className='nav-links' onClick={closeMobileMenu}>
                        Database
                    </Link>
                </li>
                <li className='nav-item'>
                    <Link to="/Model" className='nav-links' onClick={closeMobileMenu}>
                        Model
                    </Link>
                </li>
                <li className='nav-item'>
                    <Link to="/sign-up" className='nav-links-mobile' onClick={closeMobileMenu}>
                        Sign-Up
                    </Link>
                </li>
            </ul>
        </div>
    </nav>
    </>

  )
}

export default Navbar