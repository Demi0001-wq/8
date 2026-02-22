# 🎓 LMS Project

This is a **backend project** for a Learning Management System built with **Django** and **Django REST Framework**.

## 🚀 Features

- **User Management**: Secure login using **SimpleJWT**.
- **Role-Based Access**: Specialized roles like *Moderators* and *Owners* to manage course visibility and permissions.
- **Materials System**: 
  - **Courses** and **Lessons** management.
  - **Subscriptions**: Users can subscribe/unsubscribe to courses.
  - **Validation**: Automatic *YouTube link* validation for lesson videos.
- **Payments**: Full **Stripe Integration** for creating products, prices, and checkout sessions.
- **Documentation**: Interactive API docs powered by **drf-spectacular** (*Swagger* and *Redoc*).

## 🌐 Server Address

The application is deployed at: **[http://your-server-ip-or-domain](http://your-server-ip-or-domain)**

## 🛠 Tech Stack
- **Django** & **Django REST Framework**
- **SimpleJWT** (*Authentication*)
- **Stripe** (*Payments*)
- **drf-spectacular** (*API Documentation*)
- **PostgreSQL** (*Database*)
- **Redis** & **Celery** (*Async Tasks*)
- **Docker** & **Docker Compose** (*Containerization*)

## 📦 How to Setup (Local)

### Prerequisites
- **Docker** and **Docker Compose** installed.
- **Git**.

### Local Installation Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Demi0001-wq/8.git
   cd 8
   ```

2. **Create .env file**: 
   Copy `env.sample` to `.env` and fill in your unique variables.
   ```bash
   cp env.sample .env
   ```
   > [!IMPORTANT]
   > Ensure **STRIPE_API_KEY** and database credentials are set correctly in `.env`.

3. **Build and start the services**:
   This project uses `docker-compose` to manage services (*Django, PostgreSQL, Redis, Celery, and Nginx*).
   ```bash
   docker-compose up --build -d
   ```

4. **Run migrations and collect static files**:
   ```bash
   docker-compose exec backend python manage.py migrate
   docker-compose exec backend python manage.py collectstatic --no-input
   ```

5. **Access the application**:
   The application will be available at: **[http://localhost](http://localhost)** (via **Nginx**).

## 🛣 Endpoints

- **Login**: `/api/users/login/`
- **Token Refresh**: `/api/users/token/refresh/`
- **Courses**: `/api/materials/courses/`
- **Lessons**: `/api/materials/lessons/`
- **Subscribe**: `/api/materials/course/subscribe/`
- **Create Payment**: `/api/users/payments/create/`
- **Payment Status**: `/api/users/payments/status/id/`

## 🧪 Testing
Run the test suite with:
```bash
python manage.py test
```
*Note: I used `coverage` to ensure high test quality and reliability.*


## ⚙️ CI/CD and Automation

This project utilizes **GitHub Actions** for **Continuous Integration** and **Continuous Deployment** (CI/CD). 

### Workflow Steps
1. **Linting**: Runs `flake8` to ensure **PEP 8** compliance (*0 errors*).
2. **Testing**: Executes Django unit tests with temporary *PostgreSQL* and *Redis* services.
3. **Docker Build Check**: Verifies that Docker images build successfully before any deployment.
4. **Deployment**: Automatically deploys the code to the remote server on every push to **main** or **develop**.

### Remote Server Setup
1. **Install Docker**: Ensure the server has **Docker** and **Compose** installed.
2. **Project Directory**: Clone the project to `~/app/docker`.
3. **Nginx**: Included in the **Docker Compose** setup for reverse proxying on port **80**.

## 💳 Stripe Testing

Use these details to test the payment flow:

1. **API Keys**: Found in your [Stripe Dashboard](https://dashboard.stripe.com/test/apikeys).
2. **Test Cards**:
   - **Success Card**: `4242 4242 4242 4242`, CVC: `any`, Exp: `future date`.
   - **International Card**: `4000 0566 5443 4554` (*for foreign currencies*).

### GitHub Secrets Configuration
Add these to your **GitHub Settings > Secrets and variables > Actions**:
- `DJANGO_SECRET_KEY`: *Your production secret key.*
- `STRIPE_API_KEY`: *Your Stripe test secret key (`sk_test_...`).*
- `SERVER_HOST`: *Remote server IP/Domain.*
- `SERVER_USER`: *SSH username.*
- `SERVER_SSH_KEY`: *Private SSH key.*

---

## 📝 Submission
The project is submitted via **Pull Request** from **develop** to **main**.

**[View Final Pull Request](https://github.com/Demi0001-wq/8/compare/main...develop?expand=1)**
