from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator  

# Create your models here.

class Review(models.Model):
    """
    Stores a single review entry related to :model: `auth.user`
    """

    review_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name = 'reviewer'
    )
    star_rating = models.IntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)],
    )
    review_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='review_likes')
    
    class Meta:
        ordering = ['-created_on']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"Review by {self.review_name}"