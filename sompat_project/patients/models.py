from django.db import models

# Create your models here.
class Pacient(models.Model):
    som_id = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.som_id

class Aparat(models.Model):
    RES_IBREEZE_AUTO_CPAP = 'RES_IBREEZE_AUTO_CPAP'
    LOEWENSTEIN_PRISMA_AUTO_CPAP = 'LOEWENSTEIN_PRISMA_AUTO_CPAP'

    APARATI_CHOICES = (
        (RES_IBREEZE_AUTO_CPAP, 'Resvent iBreeze Auto CPAP'),
        (LOEWENSTEIN_PRISMA_AUTO_CPAP, 'Loewenstein Prisma Auto CPAP')
    )

    model = models.CharField(max_length=128, choices=APARATI_CHOICES, default=RES_IBREEZE_AUTO_CPAP)
    sn = models.CharField(max_length=128, unique=True)
    aktiven = models.BooleanField(default=False)

    def __str__(self):
        return self.sn
