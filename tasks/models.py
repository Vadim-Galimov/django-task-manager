from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название задачи")
    description = models.TextField(blank=True, verbose_name="Описание")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Задача"
        verbose_name_plural = "Задачи"
