from rest_framework import serializers
from .models import *


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = 'id name '.split()


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = 'id user text stars manga'.split()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = 'id full_name'.split()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'id name'.split()


class MangaSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tip = TipSerializer()
    manga_review = ReviewSerializer(many=True, read_only=True)
    genre_list = serializers.SerializerMethodField()
    genre = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    class Meta:
        model = Manga
        fields = 'id title image description status_release status_translate ' \
                 'number_of_chapters created genre_list manga_review tip author updated release_year ' \
                 'rating views genre'.split()

    def get_genre_list(self, manga_object):
        return [i.name for i in manga_object.genre.all()]

    def create(self, validated_data):
        genres_data = validated_data.pop('genres', None)
        author_data = validated_data.pop('author', None)
        tip_data = validated_data.pop('tip', None)

        author, created = Author.objects.get_or_create(**author_data) if author_data else (None, False)
        tip, created = Tip.objects.get_or_create(**tip_data) if tip_data else (None, False)

        manga = Manga.objects.create(author=author, tip=tip, **validated_data)
        if genres_data:
            manga.genre.set(genres_data)
        return manga
