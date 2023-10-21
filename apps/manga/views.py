
from .filters import MangaFilter
from .paginations import MangaPagination, ReviewPagination
from .permissions import IsAuthicatedOrReadOnly
from .serializers import *
from .models import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class MangaViewSet(ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    pagination_class = MangaPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = MangaFilter


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = PageNumberPagination


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthicatedOrReadOnly]
    pagination_class = ReviewPagination



class TipViewSet(ModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    pagination_class = PageNumberPagination
