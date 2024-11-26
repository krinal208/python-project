from django.db import models

# Create your models here.
class Contact(models.Model):
	srno = models.CharField(max_length = 100)
	album_title = models.CharField(max_length = 100)
	album_artist = models.CharField(max_length = 100)
	album_genre = models.CharField(max_length = 100)
	album_relese_year = models.CharField(max_length = 100)
	song_title = models.CharField(max_length = 100)
	song_artist = models.CharField(max_length = 100)
	song_genre = models.CharField(max_length = 100)
	song_relese_year = models.CharField(max_length = 100)
	