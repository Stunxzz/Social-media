from django.db import models
from django.conf import settings

from Profiles.models import UserProfile


class ProfilePicture(models.Model):
    user_profile = models.OneToOneField('Profiles.UserProfile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Album(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserImage(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    image = models.ImageField(upload_to='user_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded at {self.uploaded_at}"


class Post(models.Model):
    user_profile = models.ForeignKey('Profiles.UserProfile', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_profile = models.ForeignKey('Profiles.UserProfile', on_delete=models.CASCADE)
    pictures = models.ManyToManyField(UserImage, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Emoticon(models.Model):
    LIKE = 'like'
    HEART = 'heart'
    SMILE = 'smile'
    RAGE = 'rage'

    EMOTICON_CHOICES = [
        (LIKE, 'Like'),
        (HEART, 'Heart'),
        (SMILE, 'Smile'),
        (RAGE, 'Rage'),
    ]

    emoticon_type = models.CharField(max_length=10, choices=EMOTICON_CHOICES)
    related_user_img = models.ForeignKey(UserImage, on_delete=models.CASCADE)
    related_profile_img = models.ForeignKey(ProfilePicture, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    related_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

