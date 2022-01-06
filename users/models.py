from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Biodata(models.Model):
    #Cascada berarti ketika user kita delete maka biodatanya juga akan terhapus
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    telp = models.CharField(max_length=16, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.telp)

#agar penulisan didashbord admin tidak ada penambahan s seoerti biodatas
    class Meta:
        verbose_name_plural ="Biodata"

class API(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
