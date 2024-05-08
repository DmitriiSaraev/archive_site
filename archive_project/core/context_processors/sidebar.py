from archive.models import Post


def sidebar(request):
    sidebar = Post.objects.filter(type_post='sidebar')

    return {'sidebar': sidebar, }
