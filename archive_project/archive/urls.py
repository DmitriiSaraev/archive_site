from django.urls import path

from archive import views


app_name = 'archive'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('querys/', views.querys, name='querys'),
    path('organizaziyam/', views.organizaziyam, name='organizaziyam'),
    path('kalendar/', views.kalendar, name='kalendar'),
    path('reading_room/', views.reading_room, name='reading_room'),
    path('exhibitions/', views.exhibitions, name='exhibitions'),
    path('articles/', views.articles, name='articles'),
]
