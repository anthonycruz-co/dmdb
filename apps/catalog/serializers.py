from rest_framework import serializers

from apps.catalog import models


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Movie
        fields = [
            'id',
            'title',
            'release_year',
            'directors',
            'producers',
            'casting',
        ]




class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Person
        fields = [
            'last_name',
            'first_name',
        ]

