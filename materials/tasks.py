from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from celery import shared_task

from materials.models import Course, Subscription

@shared_task
def send_course_update_email(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(course=course)

    recipient_list = [sub.user.email for sub in subscriptions if sub.user.email]

    if recipient_list:
        send_mail(
            subject=f"Обновление курса: {course.title}",
            message=f"Курс '{course.title}' обновлен! Ознакомьтесь с новыми материалами.",
            from_email=EMAIL_HOST_USER,
            recipient_list=recipient_list,
        )