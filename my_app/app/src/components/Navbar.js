import {FaBars, FaTimes} from "react-icons/fa";
import { useRef } from "react";
import "../Styles/main.css";
import { NavLink } from "react-router-dom";

import React from 'react';

const Navbar = () => {
    const navRef = useRef();

    const showNavbar = () => {
        navRef.current.classList.toggle("responsive_nav")
    }

  return (
    <>
        <header>
            <h3>Logo</h3>
            <nav ref={navRef}>
                <NavLink className="link" to='/'>
                    Home
                </NavLink>
                <NavLink className="link" to='/login'>
                    Login
                </NavLink>
                <NavLink className="link" to='/register'>
                    Register
                </NavLink>
                <NavLink className="link" to='/profile'>
                    Profile
                </NavLink>
                <NavLink className="link" to='/inventory'>
                    Inventory
                </NavLink>
                <NavLink className="link" to='/allbobs'>
                    All Bobs
                </NavLink>
                <button className="nav-btn nav-close-btn" onClick={showNavbar}>
                    <FaTimes/>
                </button>
            </nav>
            <button className="nav-btn" onClick={showNavbar}>
                <FaBars /> 
            </button>
        </header>
    </>
  );
};

export default Navbar;
