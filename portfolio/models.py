from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='profiles/photos/')
    bio = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('portfolio:profile_detail', kwargs={'username': self.user.username})


class Photo(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photos/')
    tags = models.CharField(max_length=100, blank=True)
    nudity_checked = models.BooleanField(default=False)

    def __str__(self):
        return f"Photo for {self.profile.user.username}"


class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.photo}"
