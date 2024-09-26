from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    suggested_titles = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title if self.title else "Untitled Post"

