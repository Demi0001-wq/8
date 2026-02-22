from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_course_update_email(course_id, user_email):
    """Sends an email to the user when a course they are subscribed to is updated."""
    send_mail(
        subject='Course Updated',
        message=f'The course with ID {course_id} has been updated.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        fail_silently=False,
    )
