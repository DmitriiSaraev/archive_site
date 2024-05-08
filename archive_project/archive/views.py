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
    context['news'] = news

    return render(request, 'archive/pages/news.html', context)


def about(request):
    context = {}

    about_archive = Post.objects.filter(type_post='about_archive').first()
    context['about_archive'] = about_archive

    return render(request, 'archive/pages/about.html', context)


def querys(request):
    context = {}

    querys_t = Post.objects.filter(type_post='requests_t').first()
    querys_sp = Post.objects.filter(type_post='requests_sp').first()

    context['querys_t'] = querys_t
    context['querys_sp'] = querys_sp

    return render(request, 'archive/pages/querys.html', context)


def organizaziyam(request):
    context = {}
    mode = OperatingMode.objects.filter(name='Для источников')
    links = Link.objects.filter(type_link='Для источников')

    context['mode'] = mode
    context['links'] = links

    return render(request, 'archive/pages/organizaziyam.html', context)


def kalendar(request):
    context = {}

    kalendars = Link.objects.filter(type_link='Календарь')

    context['kalendars'] = kalendars

    return render(request, 'archive/pages/kalendar.html', context)


def reading_room(request):
    context = {}

    reading_room = Post.objects.filter(type_post='reading_room').first()
    books_list = ListBooks.objects.all()

    context['reading_room'] = reading_room
    context['books_list'] = books_list

    return render(request, 'archive/pages/reading_room.html', context)


def exhibitions(request):
    context = {}
    exhibitions = Post.objects.filter(type_post='exhibitions')

    context['exhibitions'] = exhibitions

    return render(request, 'archive/pages/exhibitions.html', context)


def articles(request):
    context = {}
    articles = Post.objects.filter(type_post='article')

    context['articles'] = articles

    return render(request, 'archive/pages/articles.html', context)


def docs(request):
    context = {}

    docs = Link.objects.filter(type_link='docs')

    context['docs'] = docs

    return render(request, 'archive/pages/docs.html', context)


def contacts(request):
    context = {}

    main_post = Post.objects.filter(type_post='main_them').first()
    contacts = Contacts.objects.filter(name='Контакты').first()
    operating_mode = (OperatingMode.objects.filter(name='Режим работы').
                      order_by('number'))

    context['main_post'] = main_post
    context['contacts'] = contacts
    context['operating_mode'] = operating_mode

    return render(request, 'archive/pages/contacts.html', context)













