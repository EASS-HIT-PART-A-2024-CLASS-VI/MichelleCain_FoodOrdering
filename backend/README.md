# 🥡 Food Ordering System - Backend  

This repository contains the backend for a **Food Ordering System** built using **FastAPI**. It enables users to place food orders, manage menu items, and handle related functionalities efficiently, all while adhering to **SOLID principles** for clean and modular design.  

---

## 🚀 Features  

- **🛒 Food Order Management**: Create and manage food items seamlessly.  
- **📋 Menu Management**: Add, update, and delete menu items with ease.  
- **🧪 Test Integration**: Comprehensive tests to ensure application robustness.  
- **🐳 Docker Support**: Ready for containerization for hassle-free deployment and scaling.  

---

## 🛠️ Technologies Used  

- **🌐 FastAPI**: Modern, high-performance web framework for APIs.  
- **⚡ Uvicorn**: Blazing-fast ASGI server for serving the app.  
- **✅ Pydantic**: Simplifies data validation and settings management.  
- **🐋 Docker**: Containerization for portability and scalability.  
- **🧪 pytest**: Unit and integration testing framework.  

---

## 📂 Project Structure  

```plaintext
.
├── backend
│   ├── app
│   │   ├── __init__.py         # Package initializer
│   │   ├── crud.py             # Database operations
│   │   ├── database.py         # Database connection setup
│   │   ├── main.py             # FastAPI application entry point
│   │   ├── models.py           # Database models
│   │   ├── schemas.py          # Pydantic schemas for validation
│   │   ├── unit_tests.py       # Unit tests for API endpoints
│   │   └── requirements.txt    # Python dependencies
│   ├── Dockerfile              # Docker configuration
│   ├── integration_test.py     # Integration tests for the app
│   └── requirements.txt        # Project-wide dependencies
├── README.md                   # Project documentation
└── .DS_Store                   # MacOS metadata file (can be ignored)

```

---

## **📥 Installation**

Prerequisites
Ensure Python 3.9+ is installed. Download it here.

Steps

Clone the Repository:
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository

Create a Virtual Environment:
python3 -m venv venv
Activate the Virtual Environment:

Windows:
.\venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

Install Dependencies:
pip install -r requirements.txt


---

## ▶️ **Running the Application**
Start the FastAPI application:

uvicorn backend.app.main:app --host 0.0.0.0 --port 8000

Visit the app at http://localhost:8000.


---

## **🧪 Running Tests**
Run unit and integration tests with the following command:

pytest

To run specific tests:
pytest path/to/test_file.py


---

## **🐳 Docker Support**
Build the Docker Image:

docker build -t food-ordering-backend .

Run the Docker Container:

docker run -d -p 8000:8000 food-ordering-backend

Access the app at http://localhost:8000.


---

## 🙌 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests
For more information on FastAPI, visit: https://fastapi.tiangolo.com/
For more information on Docker, visit: https://www.docker.com/

