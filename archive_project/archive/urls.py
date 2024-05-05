from django.urls import path

from archive import views


app_name = 'archive'

urlpatterns = [
    path('', views.index, name='index')
]