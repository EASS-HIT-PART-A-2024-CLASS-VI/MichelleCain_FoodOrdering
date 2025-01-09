// 1. יצירת הזמנה חדשה
document.getElementById('createOrderForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const quantity = document.getElementById('quantity').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/orders', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, quantity }),
        });

        if (!response.ok) {
            throw new Error('Failed to add order');
        }

        const result = await response.json();
        alert(result.message);

    } catch (error) {
        console.error('Error:', error);
    }
});

// 2. הצגת כל ההזמנות מה-API
async function getOrders() {
    try {
        const response = await fetch('http://127.0.0.1:8000/orders');
        if (!response.ok) {
            throw new Error('Failed to fetch orders');
        }
        const orders = await response.json();
        displayOrders(orders.orders);
    } catch (error) {
        console.error('Error:', error);
    }
}

function displayOrders(orders) {
    const ordersList = document.getElementById('ordersList');
    ordersList.innerHTML = '';
    orders.forEach(order => {
        const orderDiv = document.createElement('div');
        orderDiv.textContent = `Name: ${order.name}, Quantity: ${order.quantity}`;
        ordersList.appendChild(orderDiv);
    });
}

// 3. חיפוש לפי שם או קטגוריה
document.getElementById('searchBtn').addEventListener('click', async function() {
    const searchName = document.getElementById('searchName').value;

    try {
        const response = await fetch(`http://127.0.0.1:8000/orders/search?name=${searchName}`);
        if (!response.ok) {
            throw new Error('Failed to search orders');
        }
        const searchResults = await response.json();
        displaySearchResults(searchResults.orders);
    } catch (error) {
        console.error('Error:', error);
    }
});

function displaySearchResults(results) {
    const searchResultsDiv = document.getElementById('searchResults');
    searchResultsDiv.innerHTML = '';
    if (results.length === 0) {
        searchResultsDiv.textContent = 'No orders found';
    } else {
        results.forEach(order => {
            const resultDiv = document.createElement('div');
            resultDiv.textContent = `Name: ${order.name}, Quantity: ${order.quantity}`;
            searchResultsDiv.appendChild(resultDiv);
        });
    }
}

// ראשית מבצעים הצגת כל ההזמנות בטעינה
getOrders();

