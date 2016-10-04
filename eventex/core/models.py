from django.db import models
from django.shortcuts import resolve_url as r


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank='True')
    description = models.TextField('descriçao', blank='True')

    class Meta:
        verbose_name_plural = 'palestrantes'
        verbose_name = 'palestrante'
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)
