from django.core.paginator import Paginator


NUMBER_OF_OBJECTS_ON_PAGE = 1


def get_paginator_pages(objects, page_number):
    paginator = Paginator(objects, NUMBER_OF_OBJECTS_ON_PAGE)
    objects = paginator.page(page_number)
    return objects
