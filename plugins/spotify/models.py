from django.db import models

class SpotifyUser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username

    def login(self):
        # This function will be implemented in the views.py file
        pass

    class Meta:
        verbose_name = "Spotify User"
        verbose_name_plural = "Spotify Users"