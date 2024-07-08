from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Islam(models.Model):
    quran = models.IntegerField()
    solat_duha = models.BooleanField()
    solat_vitr = models.BooleanField()
    mechet_fard = models.BooleanField()
    tauba = models.BooleanField()
    sadaka = models.BooleanField()
    zikr_ut = models.BooleanField()
    zikr_vech = models.BooleanField()
    rodstven_otn = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="islams")


class VredPrivichki(models.Model):
    son = models.BooleanField()
    telefon = models.IntegerField()
    haram = models.BooleanField()
    eda = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="vredprivichkis")

    # def __str__(self):
    #     return self.u

class Cel(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="cels",
    )
    name = models.CharField(max_length=150)
    dt_beg = models.DateField(auto_now_add=True)
    dt_end = models.DateField(null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    cel = models.ForeignKey(
        to=Cel,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.body
