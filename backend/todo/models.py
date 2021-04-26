from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.

class Todo(models.Model):
    title = CharField(max_length=120)
    description = TextField()

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.title
