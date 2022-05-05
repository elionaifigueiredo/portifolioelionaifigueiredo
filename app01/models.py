from django.db import models

# Create your models here.


class Carro(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        db_table = 'carro'

    def __str__(self) -> str:
        return self.nome