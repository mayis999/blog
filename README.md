# Blog API

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Description

The Blog API is a backend application developed using Django and Django REST Framework. This API provides endpoints for managing blog posts, including creating, retrieving, updating, and deleting posts. The application also supports functionalities for refback and insurance related to blog posts.

## Features

- **Create Post**: Endpoint to create new blog posts.
- **Retrieve Posts**: Endpoint to retrieve a list of blog posts or details of a specific post.
- **Update Post**: Endpoint to update existing blog posts.
- **Delete Post**: Endpoint to delete blog posts.
- **Refback**: Endpoint to submit Refback on posts.
- **Insurance**: Endpoint to handle insurance-related functionalities for posts.

## Technologies

- **Python**: Programming language.
- **Django**: Web framework for building the application.
- **Django REST Framework**: For API development and authentication.
- **SQLite3**: Database for data storage.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mayis999/blog.git
    ```
2. **Set up a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```
5. **Create a superuser** (optional, for accessing the admin interface):
    ```bash
    python manage.py createsuperuser
    ```
6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- **Admin Interface**:
  - **URL**: `/admin/`
  - **Description**: Access the Django admin interface for managing the application.

- **Projects**:
  - **List/Create Projects**:
    - **URL**: `/projects/`
    - **Method**: `GET` (List all projects) / `POST` (Create a new project)
  - **Retrieve/Update/Delete Project**:
    - **URL**: `/projects/{id}/`
    - **Method**: `GET` (Retrieve a project) / `PUT` (Update a project) / `DELETE` (Delete a project)

- **Refback**:
  - **Submit Feedback**:
    - **URL**: `/refback/`
    - **Method**: `POST`
    - **Description**: Submit refback related to projects.

- **Insurance**:
  - **Handle Insurance**:
    - **URL**: `/insurance/`
    - **Method**: `POST`
    - **Description**: Handle insurance-related functionalities for projects.

## Usage

1. **Start the server** by running the `manage.py` script.
2. **Access the API** through the provided endpoints. Use tools like [Postman](https://www.postman.com) or `curl` for making API requests.
3. **Authenticate** if necessary, and interact with the API according to the available endpoints.
