from django.shortcuts import render
from archive.models import (Post, Contacts, OperatingMode, Link,
                            ListBooks, ImageForPost)


def index(request):
    context = {}

    main_link = Link.objects.filter(type_link='main').first()
    main_post = Post.objects.filter(type_post='main_them').first()
    contacts = Contacts.objects.filter(name='Контакты').first()
    operating_mode = (OperatingMode.objects.filter(name='Режим работы').
                      order_by('number'))
    reading_room = Post.objects.filter(type_post='reading_room').first()


    context['main_link'] = main_link
    context['main_post'] = main_post
    context['contacts'] = contacts
    context['operating_mode'] = operating_mode
    context['reading_room'] = reading_room

    return render(request, 'archive/pages/main.html', context)


def news(request):
    context = {}

    news = Post.objects.filter(type_post='news').select_related()
    for new in news:
        print(new)

    context['news'] = news
    print(news)
    new = news[0]
    print(new.images)

    return render(request, 'archive/pages/news.html', context)
