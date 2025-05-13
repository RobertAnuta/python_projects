from django.db import models
from django.urls import reverse


class Author(models.Model):
    pass

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    date = models.DateField()
    image = models.ImageField()
    excerpt = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])
