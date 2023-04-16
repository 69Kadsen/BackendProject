import React, { useEffect, useState } from "react";

import User from "./User";


const Inventory = () => {

    console.log("sup", User)

    const [inventory, setInventory] = useState(User.inventory);
    const [newItem, setNewItem] = useState({});


    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setNewItem({ ...newItem, [name]: value });
    };
    
    const handleSubmit = (event) => {
        event.preventDefault();
        setInventory([...inventory, newItem]);
        setNewItem({});
      };

    const addInventoryItem = async (item) => {
        const token = localStorage.getItem("token");
        const requestOptions = {
            method: "PUT",
            headers: {"Content-Type": "application/json", token: token},
            body: item
        };

        const response = await fetch("https://69kadsen-glorious-memory-5wv4wwxj6p6cpxr6-8000.preview.app.github.dev/api/user/{user.username}/inventory", requestOptions);

        if (response.ok) {
            const user = await response.json();
            setInventory(user.inventory);
        }
    };

    const inventoryList = inventory.map((item, index) => (
        <li key={index}>{item}</li>
    ));


    return (
        <>
            <h2>Inventory</h2>
            <ul>{inventoryList}</ul>

            <form onSubmit={handleSubmit}>
                <label>
                Bot Number:
                <input
                    type="number"
                    name="bot_number"
                    value={newItem.bot_number || ""}
                    onChange={handleInputChange}
                />
                </label>
                <br />
                <label>
                Claimed:
                <select name="claimed" value={newItem.claimed || ""} onChange={handleInputChange}>
                    <option value="">Select</option>
                    <option value={true}>Yes</option>
                    <option value={false}>No</option>
                </select>
                </label>
                <br />
                <label>
                Value:
                <input
                    type="number"
                    name="value"
                    value={newItem.value || ""}
                    onChange={handleInputChange}
                />
                </label>
                <br />
                <button type="submit">Add</button>
            </form>

        </>
    );
};


export default Inventory;