from django.db import models

# Create your models here.
class Pacient(models.Model):
    som_id = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.som_id

class Aparat(models.Model):
    model = models.CharField(max_length=128, unique=True)
    sn = models.CharField(max_length=128, unique=True)
    aktiven = models.BooleanField(default=False)

    def __str__(self):
        return self.sn
