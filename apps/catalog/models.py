from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class TraceMixInManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class TraceMixInModel(models.Model):

    deleted = models.BooleanField(
        default=False,
        db_index=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    object = TraceMixInManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class Movie(TraceMixInModel):

    title = models.CharField(
        max_length=120
    )

    slug = models.CharField(
        max_length=80
    )

    release_year = models.IntegerField()

    def __str__(self):
        return '{} ({})'.format(self.title, self.release_year)


class Person(TraceMixInModel):

    last_name = models.CharField(
        max_length=120
    )

    first_name = models.CharField(
        max_length=120
    )

    movies_played = models.ManyToManyField(
        'catalog.Movie',
        through='catalog.StarringBy',
        related_name='casting'
    )

    movies_as_director = models.ManyToManyField(
        'catalog.Movie',
        through='catalog.DirectedBy',
        related_name='directors'
    )

    movies_as_producer = models.ManyToManyField(
        'catalog.Movie',
        through='catalog.ProducedBy',
        related_name='producers'
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class AlsoKnownAs(models.Model):

    alias = models.CharField(
        max_length=120
    )

    person = models.ForeignKey(
        'catalog.Person',
        on_delete=models.CASCADE
    )


class Crew(models.Model):

    person = models.ForeignKey(
        'catalog.Person',
        on_delete=models.CASCADE
    )

    movie = models.ForeignKey(
        'catalog.Movie',
        on_delete=models.CASCADE
    )
    
    class Meta:
        abstract = True

    def __str__(self):
        return ''


class DirectedBy(Crew):
    pass


class ProducedBy(Crew):
    pass


class StarringBy(Crew):
    pass