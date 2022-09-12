from django.db import models
from django.contrib.auth.models import User
from pkg_resources import require

# Create your models here.
class Document(models.Model):
    create_date = models.DateField()
    save_date = models.DateField(auto_now_add=True)
    percent = models.IntegerField(default=0)
    link = models.FileField(upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.link.name