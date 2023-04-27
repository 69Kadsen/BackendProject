import React, { useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import LoginPage from './pages/Login';
import RegisterPage from './pages/Register';
import ProfilePage from './pages/Profile';
import InventoryPage from './pages/Inventory';
import AllBobsPage from './pages/Allbobs';


function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(localStorage.getItem('token') ? true : false);

  return (
      <Router>
        <Navbar isAuthenticated={isAuthenticated} setIsAuthenticated={setIsAuthenticated} />
          <Routes>
            <Route path='/' exact element={ <Home/> } />
            <Route path='/login' element={<LoginPage setIsAuthenticated={setIsAuthenticated} />} />
            <Route path='/register' element={ <RegisterPage/> } />
            <Route path='/profile' element={ <ProfilePage/> } />
            <Route path='/inventory' element={ <InventoryPage/>} />
            <Route path='/allbobs' element={ <AllBobsPage/> } />
          </Routes>
      </Router>
  );
};

export default App;
