from django.db import models
from django.shortcuts import resolve_url as r

from eventex.core.managers import KindQuerySet, PeriodManager


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


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'e-mail'),
        (PHONE, 'telefone')
    )
    speaker = models.ForeignKey('Speaker')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'

    def __str__(self):
        return self.value


class Activity(models.Model):
    title = models.CharField('título', max_length=200)
    start = models.TimeField('início', blank='True', null='True')
    description = models.TextField('descrição', blank='True')
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank='True')

    objects = PeriodManager()

    class Meta:
        abstract = True
        verbose_name_plural = 'atividades'
        verbose_name = 'atividade'

    def __str__(self):
        return self.title


class Talk(Activity):
    class Meta:
        verbose_name_plural = 'palestras'
        verbose_name = 'palestra'


class Course(Activity):
    slots = models.IntegerField()

    class Meta:
        verbose_name_plural = 'mini-cursos'
        verbose_name = 'mini-curso'
