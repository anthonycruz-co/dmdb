from rest_framework import viewsets

from apps.catalog import models
from apps.catalog import serializers


class MovieViewSet(viewsets.ModelViewSet):

    queryset = models.Movie.object.all()
    serializer_class = serializers.MovieSerializer


class PersonViewSet(viewsets.ModelViewSet):

    queryset = models.Person.object.all()
    serializer_class = serializers.PersonSerializer