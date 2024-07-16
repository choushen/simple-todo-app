from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content} - {self.createdBy} - {self.completed}"
