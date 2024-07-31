# Chaotix.AI Assignment

## Project Overview
Chaotix.AI Assignment is a Django-based application that utilizes Stability AI's Text-to-Image API to generate images asynchronously using Celery. The project is containerized using Docker and connects to a PostgreSQL database. The application also features a REST API built with Django REST Framework for managing TestUser objects.

## Features

1. **Image Generation:** Asynchronously generate images based on text prompts using Stability AI’s Text-to-Image API.
2. **Celery Integration:** Manage asynchronous tasks with Celery and Redis.
3. **PostgreSQL Database:** Store image metadata and user information.
4. **Django REST Framework:** Provide a RESTful API for managing TestUser objects.
5. **Dockerized Environment:** Containerize the application using Docker for easy deployment and scalability.
6. **Multi-Container Setup:** Use Docker Compose to manage multiple services (Django, PostgreSQL, Redis, Pgadmin,       
   Celery).

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dee077/Chaotix_ai_Assignment
   cd Chaotix_ai_Assignment
   ```
2. **Docker Compose Setup:**
   ```bash
   docker-compose up --build -d
   ```

## API Endpoints

### Generate Image
- **URL**: `/generate-image/`
- **Method**: `POST`
- **Description**: Generates images based on text prompts.
- **Request Body**:
  ```json
  {
    "no_of_images": 3,
    "prompts": ["A red flying dog", "A piano ninja", "A footballer kid"]
  }
  ```
