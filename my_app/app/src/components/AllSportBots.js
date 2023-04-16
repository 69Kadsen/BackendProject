import React, { useState, useEffect } from "react";
import SportBot from "./SportBot";

const AllBobs = () => {
  const [sportbots, setSportbots] = useState([]);

  useEffect(() => {
    const fetchSportbots = async () => {

    const response = await fetch('https://69kadsen-glorious-memory-5wv4wwxj6p6cpxr6-8000.preview.app.github.dev/api/sportbots'); // replace with your API endpoint
    const data = await response.json();
    console.log(data.data[0])
    setSportbots(data.data[0]);

    };

    fetchSportbots();
  }, []);

  return (
    <div className="container">
      <div className="row">
        {sportbots.map((sportbot, index) => (
          <div className="col-md-4 mb-3" key={`${sportbot._id}-${index}`}>
            <SportBot
              key={`${sportbot._id}-${index}`}
              name={sportbot.name}
              number={sportbot.number}
              imageUrl={sportbot.image_url}
              stats={sportbot.stats}
              traits={sportbot.traits}
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default AllBobs
