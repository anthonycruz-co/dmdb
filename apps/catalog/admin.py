from django.contrib import admin

from apps.catalog import models


class DirectedByInLine(admin.TabularInline):
    model = models.DirectedBy
    extra = 1
    verbose_name = 'Person'
    verbose_name_plural = 'Directed By'


class ProducedByInLine(admin.TabularInline):
    model = models.ProducedBy
    extra = 1
    verbose_name = 'Person'
    verbose_name_plural = 'Produced By'


class StarringByInLine(admin.TabularInline):
    model = models.StarringBy
    extra = 1
    verbose_name = 'Person'
    verbose_name_plural = 'Casting'


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'release_year'
    )

    inlines = (
        DirectedByInLine,
        ProducedByInLine,
        StarringByInLine,
    )


class MoviesAsDirectorInLine(admin.TabularInline):
    model = models.DirectedBy
    extra = 1
    verbose_name = 'Movie'
    verbose_name_plural = 'Movies As Director'


class MoviesAsProducerInLine(admin.TabularInline):
    model = models.ProducedBy
    extra = 1
    verbose_name = 'Movie'
    verbose_name_plural = 'Movies As Producer'


class MoviesPlayedInLine(admin.TabularInline):
    model = models.StarringBy
    extra = 1
    verbose_name = 'Movie'
    verbose_name_plural = 'Movies As Actress/Actor'


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'last_name',
        'first_name',
    )

    inlines = (
        MoviesAsDirectorInLine,
        MoviesAsProducerInLine,
        MoviesPlayedInLine,
    )

