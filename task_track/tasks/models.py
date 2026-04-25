from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=64)
    creator = models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='owned_projects',
                                verbose_name='Владелец')
    participants = models.ManyToManyField(User, related_name='projects',
                                          verbose_name='Участники',
                                          null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_work', 'В работе'),
        ('done', 'Выполнена')
    ]

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    priority = models.IntegerField()
    status = models.CharField(max_length=64 )
    deadline = models.DateTimeField("Дедлайн")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='created_task', verbose_name='Автор')
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 blank=True, related_name='perform_task',
                                 verbose_name='Исполнитель')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, 
                                related_name='tasks', verbose_name='Проект')

    def __str__(self):
        return f"{self.name} (Автор: {self.author})"