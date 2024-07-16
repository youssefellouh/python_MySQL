# Projet MySQL

This project is a simple web application using Flask, SQLAlchemy, and MySQL.

## Prerequisites

- Python : The programming language.
- Flask : Serves as the foundational web framework for building the application.
- SQLAlchemy: Offers an ORM layer for interacting with the database, simplifying database transactions and queries.
- mysql-connector-python (8.0.33): Provides MySQL database connectivity.
- Docker: For running MySQL in a container.

## Installation

### Clone the Repository

```bash
git clone https://github.com/youssefellouh/python_MySQL.git
cd python_MySQL 
```
### Build and Run the Application with Docker Compose
```bash
docker compose up
```
### Run the Application
```bash 
python app/app.py
```
### Project Structure
```bash 
├── app
│   ├── app.py
│   ├── static
│   │   ├── script.js
│   │   └── styles.css
│   └── templates
│       └── index.html
├── docker-compose.yaml
├── Dockerfile
├── README.md
└── requirements.txt
```


