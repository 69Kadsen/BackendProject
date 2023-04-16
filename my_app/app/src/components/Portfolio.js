import React from "react";


const Portfolio = () => {


    const get_current_user = async () => {
        const requestOptions = {
            method: "GET",
        }
        
        const response = await fetch("https://69kadsen-glorious-memory-5wv4wwxj6p6cpxr6-8000.preview.app.github.dev/api/user/me", requestOptions)
        const data = await response.json()

        if (!response.ok) {
            console.log("Error")
        } else {
            console.log("Success", data)
            navigate('/');
        }

    };

};

export default Portfolio;