# Service Request Management System

A backend application built using **FastAPI and MySQL** that allows users to submit and manage service requests through a structured API. The system provides role-based access control, enabling administrators to manage available services and oversee customer requests while regular users can browse services and submit requests.

## Features

- **User Authentication:** User registration and login with password hashing.
- **Role-Based Access Control (RBAC):** Separate permissions for Admin and Customer roles.
- **Service Management:** Administrators can create, manage, and deactivate services.
- **Service Requests:** Customers can submit service requests with relevant details.
- **Request Management:** Administrators can view, update, and manage service request statuses.
- **Database Integration:** MySQL database integration using SQLAlchemy ORM.
- **API Documentation:** Interactive API documentation using Swagger UI.
- **Environment Configuration:** Sensitive configuration and database credentials managed through environment variables.

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **Password Security:** Bcrypt Password Hashing
- **Validation & Configuration:** Pydantic, Pydantic Settings
- **API Testing:** Postman, Swagger UI
- **Containerization:** Docker

## User Roles

### Admin
- Manage available services.
- View all customer service requests.
- Update service request statuses.
- Manage service availability.

### Customer
- Register and log in.
- View available services.
- Submit new service requests.
- Access permitted service-related functionality.

## Project Purpose

The main objective of this project is to develop a structured backend system for handling customer service requests, implementing secure authentication, role-based authorization, database operations, and RESTful API development.

