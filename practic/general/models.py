from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Islam(models.Model):
    quran = models.IntegerField(default=0)
    solat_duha = models.BooleanField(default=None, null=True, blank=True)
    solat_vitr = models.BooleanField(default=None, null=True, blank=True)
    fadjr = models.BooleanField(default=None, null=True, blank=True)
    mechet_fard = models.BooleanField(default=None, null=True, blank=True)
    tauba = models.BooleanField(default=None, null=True, blank=True)
    sadaka = models.BooleanField(default=None, null=True, blank=True)
    zikr_ut = models.BooleanField(default=None, null=True, blank=True)
    zikr_vech = models.BooleanField(default=None, null=True, blank=True)
    rodstven_otn = models.BooleanField(default=None, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="islams")


class VredPrivichki(models.Model):
    son = models.BooleanField(default=None, null=True, blank=True)
    telefon = models.BooleanField(default=None, null=True, blank=True)
    haram = models.BooleanField(default=None, null=True, blank=True)
    eda = models.BooleanField(default=None, null=True, blank=True)
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
