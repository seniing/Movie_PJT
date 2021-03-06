from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # movies
    path('', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/like/', views.like_movie),

    path('popular/', views.movie_popular),
    path('genres/', views.movie_genre),

    path('like_recommend/', views.like_movies),

    # path('recommend/', views.movie_recommend),
    # path('genre_recommend/<username>/', views.genre_recommend),
    path('search/', views.search),
    # comments
    path('<int:movie_id>/comments/', views.create_comment),
    path('<int:movie_id>/comments/<int:comment_pk>/', views.comment_update_or_delete),
]