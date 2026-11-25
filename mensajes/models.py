from django.db import models


# Create your models here.
class Mensaje(models.Model):
    texto = models.TextField()
    autor = models.CharField("autor", max_length=50, default="Anónimo")
    fecha = models.DateTimeField("fecha de publicación", auto_now_add=True)

    class Meta:  # nuevo
        ordering = ["-fecha"]

    def __str__(self):  # nuevo
        return self.texto[:50]
