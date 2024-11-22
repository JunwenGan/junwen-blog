# Personal Blog Application

A full-stack personal blog application built with **Vue 3** for the frontend and **Django (Django REST Framework)** for the backend. The app allows users to view articles, post comments, and manage content through a clean, responsive interface.

## Features

- **Frontend**:
  - Display a list of blog articles.
  - View detailed article pages with comments.
  - User authentication (login) via JWT.
  - Responsive design using modern UI libraries.

- **Backend**:
  - RESTful API built with Django REST Framework.
  - JWT-based authentication.
  - Supports CRUD operations for articles and comments.
  - Pagination and CORS support for efficient and secure data fetching.

## Tech Stack

- **Frontend**: Vue 3, Vue Router, Axios, Vite
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (can be replaced with PostgreSQL or MySQL)
- **Deployment**: Supports deployment via Docker, Nginx, or Gunicorn.

## Installation

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js 16+](https://nodejs.org/en/)
- [Git](https://git-scm.com/)

### Backend Setup (Django)

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git](https://github.com/JunwenGan/junwen-blog.git
2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Apply database migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Run the development server:
   python manage.py runserver
Frontend Setup (Vue)
1. Navigate to the frontend directory:
   cd ../frontend
2. npm install
3. npm run dev


