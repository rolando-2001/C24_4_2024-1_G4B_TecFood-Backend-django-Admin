from django.db import models

class Role(models.Model):
    role_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name