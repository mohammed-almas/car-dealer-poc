# Overview
This project is a simple POC written in python with the help of FastAPI framework. It has implementations for CRUD operations for two models Dealer and Car which uses sqlite as the database and sqlalchemy as the ORM.

# Getting Started

### Prerequisites
- Python 3.8+
- Virtualenv

### Installation Steps
1. Create a virtual environment.
    ```sh
    virtualenv venv
    ```
    
2. Activate virtual env.

    For MacOS:
    ```sh
    source venv/bin/activate
    ```

    For Windows:
    ```sh
    venv/Scripts/activate
    ```

3. Install python modules from requirements.txt file using pip.
    ```sh
    pip install -r requirements.txt
    ```

### Running the project
To run the project, start the uvicorn server using the following command.
```sh
uvicorn main:app --reload
```

### API Docs
To see the Swagger documentation for the project, go to the following address in browser after running the project local server.
```
http://localhost:8000/docs
```
