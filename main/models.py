from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=222)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.title}\n{self.description}"

  #THIS LINE OF CODE IS VERY IMPORTANT, MAY NEED TO BE RE-ADDED
  #def __str__(self):
  #  return self.title + "\n" + self.description