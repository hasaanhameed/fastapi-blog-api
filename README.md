# FastAPI Blog API

A fully functional **FastAPI-based Blog API** featuring:

- JWT Authentication  
- User Registration & Login  
- Password Hashing with bcrypt  
- Blog CRUD Operations  
- SQLAlchemy ORM  
- SQLite Database (dev mode)  
- Modular Router Structure  
- Pydantic Schemas for validation  
- OAuth2 Password Flow  

This project was built as part of my FastAPI learning journey and demonstrates how to structure a real-world backend API using Python and modern best practices.

---

## Features

### Authentication & Security
- JWT access tokens  
- Password hashing (bcrypt)  
- Secure login and protected routes  
- Token verification middleware  

### User Management
- Create users  
- Fetch user profiles  
- Relationship mapping between users and blogs  

### Blog Functionality
- Create a blog  
- Read all blogs  
- Read a single blog  
- Update a blog  
- Delete a blog  
- Automatic linking to the blog creator  

### Project Structure
Blog/
├── routers/
│ ├── blog.py
│ ├── user.py
│ └── authentication.py
├── repository/
│ ├── blog.py
│ ├── user.py
│ └── authentication.py
├── models.py
├── database.py
├── hashing.py
├── oauth2.py
└── auth_token.py
main.py

## Tech Stack

- **FastAPI**
- **Python 3.10+**
- **SQLAlchemy**
- **bcrypt**
- **python-jose (JWT)**
- **SQLite**
