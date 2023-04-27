import React, { useState, useEffect } from 'react';

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
              setUser(userData);
          }
      }
      getCurrentUser();
  }, []);


  if (!user) {
    console.log("User data not found"); // for debugging
    return <div>Loading user data...</div>;
  }

  console.log(user)

  return (
    <div>
      <h2>Welcome, {user.username}!</h2>
      <p>Email: {user.email}</p>
    </div>
  );
};


export default Profile