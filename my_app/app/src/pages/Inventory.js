import React from "react";

import Inventory from "../components/Inventory";
import AddBot from "../components/AddInventoryBot";

const InventoryPage = () => {
    return(
        <div>
            <h1>Portfolio Page</h1>
            <Inventory />
            <AddBot />
        </div>
    );
};

export default InventoryPage;