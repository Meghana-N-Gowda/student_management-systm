from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)

    def _str_(self):
        return self.name
