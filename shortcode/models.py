from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
from .utils import create_shortener


class URL(models.Model):
	url = models.CharField(max_length=150)
	short = models.CharField(max_length=15, unique=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add = True)

	def save(self, *args, **kwargs):
		if self.short is None or self.short == "":
			self.short = create_shortener(self)
		super(URL, self).save(*args, **kwargs)

	def __str__(self):
		return self.url

	def get_short_url(self):
		url_path = reverse('shortview', kwargs={'short':self.short}, args=None)
		return "chort.herokuapp.com"+url_path
