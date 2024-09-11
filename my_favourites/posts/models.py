from django.db import models


class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Timestamped):
    """
    Represents a post with author, title, content, file, image and
    inherits date of creation or update from the Timestamped class.
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='posts/files/%Y/%m/%d', blank=True, null=True)
    image = models.ImageField(upload_to='posts/images/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.title}'
