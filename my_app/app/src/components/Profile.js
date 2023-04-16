import React, { useState, useEffect, useContext } from 'react';

const Profile = () => {

  const [user, setUser] = useState();

  useEffect( () => {
      async function getCurrentUser() {
          const token = localStorage.getItem("token");
          const requestOptions = {
              method: "GET",
              headers: {"token": token}
          }

          const response = await fetch('https://69kadsen-glorious-memory-5wv4wwxj6p6cpxr6-8000.preview.app.github.dev/api/users/me', requestOptions);
          if (response.ok) {
              const userData = await response.json();
              console.log("userData:", userData); // for debugging
              setUser(userData);
          }
      }
      getCurrentUser();
  }, []);


  if (!user) {
    console.log("User data not found"); // for debugging
    return <div>Loading user data...</div>;
  }

  return (
    <div>
      <h2>Welcome, {user.username}!</h2>
      <img src="" alt="Profile" />
      <p>Email: {user.email}</p>
      <p>Bot number: {user.inventory.bot_number}</p>
      <p>bot_name: {user.inventory.bot.name}</p>

    </div>
  );
};


export default Profile