from django.contrib import admin
from .models import *

admin.site.register(Manga)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Tip)