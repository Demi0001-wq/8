# LMS Project

This is a backend project for a Learning Management System made with Django and Django REST Framework.

## Features

This project includes user management where you can log in with your email. I used SimpleJWT for authentication. There are different roles like Moderators and Owners to handle who can see or edit the courses.

The materials app has Courses and Lessons. I added a way for users to subscribe to courses. I also made a validator to make sure video links are only from youtube.com.

For payments, I integrated Stripe. It can create products and prices, and then give a checkout link. You can also check the status of a payment.

Documentation is handled by drf-spectacular. You can see the Swagger or Redoc pages to check the endpoints.

## Tech Stack
- Django and DRF
- SimpleJWT for auth
- Stripe for payments
- drf-spectacular for docs
- SQLite

## How to setup (Local)

1. Install everything from requirements.txt:
   pip install -r requirements.txt

2. Put your Stripe key in config/settings.py:
   STRIPE_API_KEY = 'your_key_here'

3. Run the migrations:
   python manage.py migrate

4. You can fill some test payment data:
   python manage.py fill_payments

5. Start the server:
   python manage.py runserver

## How to setup (Docker)

1. **Create .env file**: 
   Copy `env.sample` to `.env` and fill in your variables (like `STRIPE_API_KEY`).
   ```bash
   cp env.sample .env
   ```

2. **Build and start the containers**:
   ```bash
   docker-compose up --build -d
   ```

3. **Check logs**:
   ```bash
   docker-compose logs -f backend
   ```

4. **Run migrations (if not automatic)**:
   ```bash
   docker-compose exec backend python manage.py migrate
   ```

5. **Stop containers**:
   ```bash
   docker-compose down
   ```

## Endpoints

- Login: /api/users/login/
- Token Refresh: /api/users/token/refresh/
- Courses: /api/materials/courses/
- Lessons: /api/materials/lessons/
- Subscribe: /api/materials/course/subscribe/
- Create Payment: /api/users/payments/create/
- Payment Status: /api/users/payments/status/id/

## Testing
You can run tests with:
python manage.py test

I also used coverage to check how much of the code is tested.
