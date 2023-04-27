import React, { useState } from "react";

import Inventory from "../components/Inventory";
import AddBot from "../components/AddInventoryBot";


const InventoryPage = () => {

    return(
        <div>
            <h1>Inventory Page</h1>
            <Inventory/>
            
        </div>
    );
};

export default InventoryPage;