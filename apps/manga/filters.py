from django_filters import FilterSet

from apps.manga.models import Manga


class MangaFilter(FilterSet):
    class Meta:
        model = Manga
        fields = ("title", "genre", "tip")
