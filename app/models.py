from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Korisnik(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ime=models.CharField(max_length=255, null=True, blank=True)
    prezime=models.CharField(max_length=255, null=True, blank=True)
    fotografija=models.ImageField(upload_to="images/", null=True, blank=True)
    interesi=models.CharField(max_length=255, null=True, blank=True)
    veshtini=models.CharField(max_length=255, null=True, blank=True)
    profesija=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Objava(models.Model):
    naslov=models.CharField(max_length=255)
    user=models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    sodrzina=models.TextField()
    files=models.FileField(upload_to="files/", null=True, blank=True)
    datum_kreiranje=models.DateTimeField()
    posledna_promena=models.DateTimeField()

    def __str__(self):
        return self.naslov

class Komentar(models.Model):
    sodrzina=models.TextField()
    datum=models.DateTimeField()
    user=models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    objava=models.ForeignKey(Objava, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.sodrzina

class Blokiran(models.Model):
    blokiral=models.ForeignKey(Korisnik, on_delete=models.CASCADE, related_name="blokiran")
    blokiran=models.ForeignKey(Korisnik, on_delete=models.CASCADE, related_name="blokiral")


