from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Islam(models.Model):
    quran = models.IntegerField(default=0)
    solat_duha = models.BooleanField(default=False)
    solat_vitr = models.BooleanField(default=False)
    fadjr = models.BooleanField(default=False)
    mechet_fard = models.BooleanField(default=False)
    tauba = models.BooleanField(default=False)
    sadaka = models.BooleanField(default=False)
    zikr_ut = models.BooleanField(default=False)
    zikr_vech = models.BooleanField(default=False)
    rodstven_otn = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="islams")


class VredPrivichki(models.Model):
    son = models.BooleanField(default=False)
    telefon = models.BooleanField(default=False)
    haram = models.BooleanField(default=False)
    eda = models.BooleanField(default=False)
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
