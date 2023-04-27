import React, { useEffect, useState } from "react";


const Inventory = () => {

    const [user, setUser] = useState();
    const [inventory, setInventory] = useState([]);
    const [newItem, setNewItem] = useState({});

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
                setInventory(userData.inventory);
                console.log(userData)
            }
        }
        getCurrentUser();
    }, []);
  
  
    if (!user) {
      console.log("User data not found"); // for debugging
      return <div>Loading user data...</div>;
    }


    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setNewItem({ ...newItem, [name]: value });
    };
    
    const handleSubmit = (event) => {
        event.preventDefault();
        setInventory([...inventory, newItem]);
        addInventoryItem(newItem)
        setNewItem({});
      };

    const addInventoryItem = async (item) => {
        console.log(item) // Debug
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

    const values = Object.values(inventory);
    console.log(values)

    if (user.inventory) {

        const inventoryList = Array.isArray(inventory) ? inventory.map((item, index) => (
            <>
            <li key={index}>{item.bot.name}</li>
            <li key={index}>{item.bot.number}</li>
            <div>I am something</div>
            <button>Try me</button>
            </>

        )) : null;

    return (
        <>
            <h2>Inventory</h2>
            <ul>{inventoryList}</ul>
            <h2>Add entry:</h2>
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
};


export default Inventory;