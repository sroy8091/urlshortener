from django.db import models
from django.urls import reverse
# Create your models here.
from .utils import create_shortener


class URL(models.Model):
    url = models.URLField(max_length=200)
    short = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.short is None or self.short == "":
            self.short = create_shortener(self)
        super(URL, self).save(*args, **kwargs)

    def __str__(self):
        return self.url

    def get_short_url(self):
        url_path = reverse('shortview', kwargs={'short': self.short})
        return "https://your-domain.vercel.app" + url_path
