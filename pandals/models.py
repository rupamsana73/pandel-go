from django.db import models
from django.contrib.auth.models import User


class Pandal(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    theme = models.CharField(max_length=100)
    rating = models.FloatField(default=0)  # cache avg rating

    def __str__(self):
        return self.name


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pandal = models.ForeignKey(Pandal, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user','pandal')

    def __str__(self):
        return f"{self.user.username} ❤️ {self.pandal.name}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pandal = models.ForeignKey(Pandal, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','pandal')

    def __str__(self):
        return f"{self.user.username} - {self.pandal.name} ({self.rating})"


class CrowdLevel(models.Model):
    CROWD_CHOICES = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pandal = models.ForeignKey(Pandal, on_delete=models.CASCADE)
    level = models.CharField(max_length=10, choices=CROWD_CHOICES)
    time_slot = models.CharField(max_length=20)   # no null now
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pandal.name} - {self.level} ({self.time_slot})"


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.CharField(max_length=10)  # user / bot
    created_at = models.DateTimeField(auto_now_add=True)
