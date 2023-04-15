from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


# Create your models here.
class Task(models.Model):
    NOT_STARTED = 'NS'
    IN_PROGRESS = 'IP'
    ALREADY_DONE = 'AD'
    STATUS_CHOICES = [
        (NOT_STARTED, 'Не в работе'),
        (IN_PROGRESS, 'В работе'),
        (ALREADY_DONE, 'Выполнена'),
    ]
    name = models.CharField(max_length=35, verbose_name='заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='описание')
    deadline = models.DateField(null=True, blank=True, verbose_name='крайний срок сдачи')
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks'
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='',
                check=models.Q(deadline__gt=datetime.now())
            )
        ]

    def __str__(self) -> str:
        return self.name
