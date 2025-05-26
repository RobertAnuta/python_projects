from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=80)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="post_images/")
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tag = models.ManyToManyField(Tag, related_name="tag")

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])
