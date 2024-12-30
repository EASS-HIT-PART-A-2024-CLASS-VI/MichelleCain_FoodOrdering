# Food Ordering System - Backend

This repository contains the backend for a food ordering system built using FastAPI. The system allows users to place food orders, manage menu items, and handle other related functionalities in an efficient and modular way.

## Features

- **Food Order Management**: Create and manage food items.
- **Menu Items**: Add, update, and delete menu items.
- **Test Integration**: The backend is equipped with tests to ensure the integrity and robustness of the application.
- **Docker Support**: The project can be containerized using Docker for easy deployment and scaling.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs.
- **Uvicorn**: ASGI server for serving the FastAPI application.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Docker**: Containerization for easy deployment and scaling.
- **pytest**: For running unit and integration tests.

## Project Structure

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




## Installation

### Prerequisites

Make sure you have Python 3.9+ installed. If not, you can download it from the official [Python website](https://www.python.org/downloads/).

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
Create a Virtual Environment:


python3 -m venv venv
Activate the Virtual Environment:

On Windows:
.\venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install Dependencies:


pip install -r requirements.txt
Running the Application
To run the FastAPI application, use the following command:

uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
The application will be accessible at http://localhost:8000.

Running Tests
To run the unit and integration tests, use the following command:

pytest
Docker
To build and run the application with Docker, use the following commands:

Build the Docker Image:

docker build -t food-ordering-backend .
Run the Docker Container:


docker run -d -p 8000:8000 food-ordering-backend
The application will be accessible at http://localhost:8000 in your browser.

