from django.db import models
from apps.authentication.models import User

Mood = [
    ('😊', 'happy'),
    ('😢', 'sad'),
    ('😡', 'angry'),
    ('🥰', 'loved'),
    ('🙄', 'annoyed'),
    ('🙃', 'confused')
]

Weather = [
    ('🌞', 'sunny'),
    ('🌥', 'cloudy'),
    ('🌧', 'raining')
]

class Entry(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    mood = models.CharField(choices=Mood, default='happy', max_length=50)
    weather = models.CharField(choices=Weather, default='sunny', max_length=50)
    text = models.TextField()
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        return str(self.owner)