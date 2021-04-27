from django.db import models

class Coffe(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    email = models.CharField(max_length=25)
    payment_id = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name
