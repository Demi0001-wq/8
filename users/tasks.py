from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import User


@shared_task
def check_user_activity():
    """
    Checks user activity and deactivates users who haven't logged in for more than a month.
    """
    one_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)

    for user in inactive_users:
        user.is_active = False
        user.save()
        print(f"User {user.email} deactivated due to inactivity.")
