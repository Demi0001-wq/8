# LMS Project

This is a backend project for a Learning Management System made with Django and Django REST Framework.

## Features

This project includes user management where you can log in with your email. I used SimpleJWT for authentication. There are different roles like Moderators and Owners to handle who can see or edit the courses.

# LMS Project

This is a backend project for a Learning Management System made with Django and Django REST Framework.

## Features

This project includes user management where you can log in with your email. I used SimpleJWT for authentication. There are different roles like Moderators and Owners to handle who can see or edit the courses.

The materials app has Courses and Lessons. I added a way for users to subscribe to courses. I also made a validator to make sure video links are only from youtube.com.

For payments, I integrated Stripe. It can create products and prices, and then give a checkout link. You can also check the status of a payment.

Documentation is handled by drf-spectacular. You can see the Swagger or Redoc pages to check the endpoints.

## Server Address

The application is deployed at: [http://your-server-ip-or-domain](http://your-server-ip-or-domain)

## Tech Stack
- Django and DRF
- SimpleJWT for auth
- Stripe for payments
- drf-spectacular for docs
- SQLite

## How to setup (Local)

### Prerequisites
- Docker and Docker Compose installed.
- Git.

### Local Installation Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Demi0001-wq/docker.git
   cd docker
   ```

2. **Create .env file**: 
   Copy `env.sample` to `.env` and fill in your variables.
   ```bash
   cp env.sample .env
   ```
   > [!IMPORTANT]
   > Ensure `STRIPE_API_KEY` and database credentials are set correctly in `.env`.

3. **Build and start the services**:
   This project uses `docker-compose` to manage services (Django, PostgreSQL, Redis, Celery, and Nginx).
   ```bash
   docker-compose up --build -d
   ```

4. **Run migrations and collect static files**:
   ```bash
   docker-compose exec backend python manage.py migrate
   docker-compose exec backend python manage.py collectstatic --no-input
   ```

5. **Access the application**:
   The application will be available at [http://localhost](http://localhost) (via Nginx).

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


## CI/CD and Automation

This project uses **GitHub Actions** for continuous integration and continuous deployment (CI/CD). The workflow is defined in `.github/workflows/deploy.yml`.

### Workflow Steps
1.  **Linting**: Runs `flake8` to ensure code quality.
2.  **Testing**: Runs Django unit tests with a temporary PostgreSQL and Redis setup.
3.  **Docker Build Check**: Verifies that Docker images can be built successfully before deployment.
4.  **Deployment**: If all previous steps pass, the code is automatically deployed to the remote server on every push to `main` or `develop`.

### Remote Server Setup

1.  **Install Docker & Compose**: Ensure the server has Docker and Docker Compose installed.
2.  **Project Directory**: Clone the project to `~/app/docker`.
3.  **Nginx/Reverse Proxy**: Nginx is included in the Docker Compose setup to handle incoming traffic on port 80.

### GitHub Secrets Configuration

Add these to your GitHub repo secrets (**Settings > Secrets and variables > Actions**):

- `DJANGO_SECRET_KEY`: Your production secret key.
- `SERVER_HOST`: Remote server IP/Domain.
- `SERVER_USER`: SSH username.
- `SERVER_SSH_KEY`: Private SSH key for deployment.
- `SERVER_SSH_PASSPHRASE`: (Optional) SSH key passphrase.

---

## Submission
The project is submitted via Pull Request from `develop` to `main`.

[View Pull Request](https://github.com/Demi0001-wq/docker/pull/3)
