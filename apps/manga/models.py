from django.db import models

from apps.manga.constants import CHOICES


class Tip(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class Manga(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status_release = models.CharField(max_length=20)
    status_translate = models.CharField(max_length=20)
    number_of_chapters = models.IntegerField(default=0)
    release_year = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def rating(self):
        count = self.manga_review.count()
        if count == 0:
            return 'мангу пока никто не читал'
        total = 0
        for i in self.manga_review.all():
            total += i.stars
        return total / count

    @property
    def chapters(self):
        if self.number_of_chapters < 1:
            return "chapter didn't come out"
        return self.number_of_chapters




class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices=CHOICES)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE,
                              related_name='manga_review')

    def __str__(self):
        return self.text
