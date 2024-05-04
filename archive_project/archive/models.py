from django.db import models


class Post(models.Model):
    """
    Главная модель, основной контент (посты, новости, статьи)
    """
    TYPE_CHOICES = [
        ('main_them', 'Основной пост на главной'),
        ('about_archive', 'Об архиве'),
        ('news', 'Новости'),
        ('article', 'Статьи'),
        ('exhibitions', 'Выставки'),
        ('reading_room', 'Читальный зал'),
        ('requests_ls', 'запросы л/с'),
        ('requests_sp', 'запросы соц. пр.'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    type_post = models.CharField(max_length=100, choices=TYPE_CHOICES)
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True,
                            null=True)
    image = models.ImageField(blank=True,
                              null=True,
                              upload_to='archive')
    link = models.CharField(max_length=200,
                            blank=True,
                            null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Пост {self.name}, тип {self.type_post}'


class Contacts(models.Model):
    """
    Контакты, адрес
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    address = models.TextField()
    boss = models.CharField(max_length=100)
    senior_archivist = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'Контакты {self.name}'


class OperatingMode(models.Model):
    """
    Режим работы архива, время работы до обеда и после.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=250,
                             blank=True,
                             null=True)
    name_day = models.CharField(max_length=50,
                                blank=True,
                                null=True)
    start_time_morning = models.CharField(max_length=50,
                                          blank=True,
                                          null=True)
    end_time_morning = models.CharField(max_length=50,
                                        blank=True,
                                        null=True)
    start_time_lunch = models.CharField(max_length=50,
                                        blank=True,
                                        null=True)
    end_time_lunch = models.CharField(max_length=50,
                                      blank=True,
                                      null=True)
    text = models.TextField(blank=True,
                            null=True)

    def __str__(self):
        return 'Режим работы архива'


class Link(models.Model):
    """
    Ссылки, по типу ссылки
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    type_link = models.CharField(max_length=250)
    url = models.URLField

    def __str__(self):
        return f'Сслыка на {self.name}'


class ListBooks(models.Model):
    numb = models.IntegerField()
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    publishing = models.CharField(max_length=255)

    def __str__(self):
        return f'Книга из чит. зала номер {self.numb}'
