from django.db import models

class Post(models.Model):
    content = models.TextField(verbose_name='내용')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content