from django.db import models


class Raca(models.Model):
    raca = models.CharField(max_length=50)

    def __str__(self):
        return self.raca
