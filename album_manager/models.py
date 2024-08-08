from django.db import models

# Create your models here.

class Artist(models.Model):
    id_artist = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Album(models.Model):
    id_album = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False)
    year = models.PositiveIntegerField(null=False)
    gender = models.CharField(max_length=100, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    front_page = models.ImageField(upload_to='media/album_images/')

    def __str__(self):
        return self.title
