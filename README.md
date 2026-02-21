# LMS Backend (Django REST Framework)

A robust Learning Management System (LMS) backend built with Django and Django REST Framework. This project features a custom user model, a dedicated materials application with hierarchical lesson structure, and demonstration of multiple API architectural patterns.

## 🚀 Features

### 👤 Custom User Management
- **Email Authentication**: Replaces the default Django username with email-based login.
- **Extended Profiles**: Includes fields for `telephone`, `city`, and `avatar`.

### 🎓 Learning Materials (`materials` app)
- **Course & Lesson Relationship**: Lessons are organized under Courses using standard ForeignKey relationships.
- **Hierarchical Content**: Supports descriptions, preview images, and video links for educational value.

### 🛠️ API Architecture
- **ViewSet Pattern**: `Course` CRUD is implemented using `ModelViewSet` for rapid development and standard REST conventions.
- **Generic View Pattern**: `Lesson` CRUD is implemented using granular Generic views (`CreateAPIView`, `ListAPIView`, etc.) for maximum control.
- **Serializers**: Simple, efficient `ModelSerializer` implementations.

## 📦 Tech Stack
- **Framework**: Django 5.x
- **API**: Django REST Framework (DRF)
- **Image Handling**: Pillow
- **Database**: SQLite (Default)

## 🛠️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Demi0001-wq/DRF.git
   cd DRF
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start the server**:
   ```bash
   python manage.py run_server
   ```

## 🔗 API Endpoints

### Courses
- `GET /api/materials/courses/` - List all courses
- `POST /api/materials/courses/` - Create a course
- `PUT /api/materials/courses/<id>/` - Update a course

### Lessons
- `GET /api/materials/lessons/` - List all lessons
- `POST /api/materials/lessons/create/` - Create a lesson
- `GET /api/materials/lessons/<id>/` - Retrieve a lesson
- `PUT /api/materials/lessons/update/<id>/` - Update a lesson
- `DELETE /api/materials/lessons/delete/<id>/` - Delete a lesson

## 🧪 Testing
A comprehensive **Postman Guide** is available in the project documentation for local endpoint verification.
