from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model
    """
    TAG_CHOICES = [
      ('tribal', 'Tribal'),
      ('geometric', 'Geometric'),
      ('realism', 'Realism'),
      ('portraits', 'Portraits'),
      ('illustrative', 'Illustrative'),
      ('dotwork', 'Dotwork'),
      ('watercolour', 'Watercolour'),
      ('neo-traditional', 'Neo-traditional'),
      ('abstract', 'Abstract'),
      ('animals', 'Animals'),
      ('lettering', 'Lettering'),
      ('traditional', 'Traditional')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    image_tags = models.CharField(max_length=50, choices=TAG_CHOICES, blank=True, null=True)



    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
