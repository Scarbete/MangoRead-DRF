from django.urls import path, include

from . import views

get_post = {
        'get': 'list', 'post': 'create',
    }
id_post = {
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    }

urlpatterns = [

    path('manga/', views.MangaViewSet.as_view(get_post)),
    path('manga/<int:pk>/', views.MangaViewSet.as_view(id_post)),
    path('author/', views.AuthorViewSet.as_view(get_post)),
    path('author/<int:pk>/', views.AuthorViewSet.as_view(id_post)),
    path('genre/', views.GenreViewSet.as_view(get_post)),
    path('genre/<int:pk>/', views.GenreViewSet.as_view(id_post)),
    path('review/', views.ReviewViewSet.as_view(get_post)),
    path('review/<int:pk>', views.ReviewViewSet.as_view(id_post)),
    path('tip/', views.TipViewSet.as_view(get_post)),
    path('tip/<int:pk>', views.TipViewSet.as_view(id_post)),
]
