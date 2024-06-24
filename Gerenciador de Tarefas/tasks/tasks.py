from celery import shared_task
from django.core.mail import send_mail
from .models import Task

@shared_task
def send_reminder_email(task_id):
    task = Task.objects.get(id=task_id)
    send_mail(
        'Lembrete de Tarefa',
        f'Sua tarefa "{task.title}" está próxima do prazo.',
        'from@example.com',
        [task.user.email],
        fail_silently=False,
    )
