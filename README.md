# E-commerce API

Backend REST API for e-commerce, built with FastAPI and MongoDB.

## Features

*   **Products:** CRUD operations for product management.
*   **Users:** User registration and retrieval.
*   **Orders:** Order placement and retrieval by user.

## Technologies

*   [FastAPI](https://fastapi.tiangolo.com/)
*   [MongoDB](https://www.mongodb.com/)
*   [Motor AsyncIO](https://motor.readthedocs.io/en/stable/)
*   [Python](https://www.python.org/)
*   [Pydantic](https://pydantic-docs.readthedocs.io/en/stable/)
*   [bcrypt](https://pypi.org/project/bcrypt/)
  
## DEMO
![image](https://github.com/user-attachments/assets/f5e86a4d-c2f5-4d03-ab61-d932d8e69ee3)

## Installation

```bash
git clone <repository-url>
cd <project-directory>
python3 -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt
Configuration
MongoDB URI: Set in connect.py. Update placeholder URI.
Running
Bash

uvicorn main:app --reload
API Docs: http://127.0.0.1:8000/docs
