from django.db import models

class Produs(models.Model):
    nume = models.CharField(max_length=100)
    descriere = models.TextField()
    imagine = models.ImageField(upload_to="produse/")

    def __str__(self):
        return self.nume
