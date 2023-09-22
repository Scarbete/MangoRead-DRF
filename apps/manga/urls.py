from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MangaViewSet, AuthorViewSet, GenreViewSet, TipViewSet, ReviewViewSet

router = DefaultRouter()
router.register('manga', MangaViewSet)
router.register('author', AuthorViewSet)
router.register('genre', GenreViewSet)
router.register('tip', TipViewSet)
router.register('review', ReviewViewSet)

urlpatterns = router.urls
