from django.db import models
from django.contrib.auth.models import User
from tasks.models import Project, Task

# Create your models here.
class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новый'),
        ('On fiction', 'Фиксится'),
        ('Done', 'Готов')
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Низкий'),
        ('Medium', 'Средний'),
        ('High', 'Высокий'),
        ('Extreme', 'Экстремальный')
    ]

    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name = 'Projects',
        on_delete = models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name = 'Tasks',
        on_delete = models.SET_NULL,
        null = True
    )

    status = models.CharField(
        max_length = 50,
        choices = STATUS_CHOICES,
        default = 'New'
    )

    priority = models.CharField (
        max_length = 50,
        choices = PRIORITY_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новый'),
        ('Review', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено')
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Низкий'),
        ('Medium', 'Средний'),
        ('High', 'Высокий'),
        ('Extreme', 'Экстремальный')
    ]

    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name = 'Project',
        on_delete = models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name = 'Task',
        on_delete = models.SET_NULL,
        null = True
    )
    status = models.CharField(
        max_length = 50,
        choices = STATUS_CHOICES,
        default = 'New'
    )
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)