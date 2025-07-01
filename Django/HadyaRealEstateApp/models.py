from django.utils.text import slugify
from django.db import models
import itertools

class Property(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='properties/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            for i in itertools.count(1):
                if not Property.objects.filter(slug=slug).exists():
                    break
                slug = f'{base_slug}-{i}'
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
