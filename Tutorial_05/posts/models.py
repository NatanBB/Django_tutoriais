from django.db import models

# posts/models.py

class Post(models.Model):
  text = models.TextField()

  def __str__(self):
    return self.text[:50]