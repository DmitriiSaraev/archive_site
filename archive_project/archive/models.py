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
        ('requests_t', 'запросы тематические'),
        ('requests_sp', 'запросы соц. пр.'),
        ('external_reference', 'внешние ссылки'),
        ('sotrydniki', 'Сотрудники архива'),
        ('sidebar', 'Сайдбар'),
    ]

    name = models.CharField(max_length=200,
                            verbose_name='Имя')
    slug = models.SlugField(max_length=200)
    type_post = models.CharField(max_length=100, choices=TYPE_CHOICES,
                                 verbose_name='Тип поста')
    title = models.CharField(max_length=250,
                             verbose_name='Заголовок')
    text = models.TextField(blank=True,
                            null=True,
                            verbose_name='Основной текст')
    text_link = models.CharField(max_length=200,
                                 null=True,
                                 blank=True,
                                 verbose_name='Текст ссылки')
    link = models.CharField(max_length=200,
                            blank=True,
                            null=True,
                            verbose_name='Адрес ссылки')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'Пост {self.name}, тип {self.type_post}'


class Contacts(models.Model):
    """
    Контакты, адрес
    """
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255)
    address = models.TextField(verbose_name='Адрес')
    boss = models.CharField(max_length=100,
                            verbose_name='Начальник архива')
    senior_archivist = models.CharField(max_length=100,
                                        verbose_name='Старший архивист')
    telephone = models.CharField(max_length=50,
                                 verbose_name='Телефон')
    email = models.EmailField()

    def __str__(self):
        return f'Контакты {self.name}'


class OperatingMode(models.Model):
    """
    Режим работы архива, время работы до обеда и после.
    """
    name = models.CharField(max_length=100,
                            verbose_name='Название')
    number = models.IntegerField(verbose_name='Порядковый номер дня')
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=250,
                             blank=True,
                             null=True,
                             verbose_name='Заголовок')
    name_day = models.CharField(max_length=50,
                                blank=True,
                                null=True,
                                verbose_name='День недели')
    start_time_morning = models.CharField(max_length=50,
                                          blank=True,
                                          null=True,
                                          verbose_name='Начало работы')
    end_time_morning = models.CharField(max_length=50,
                                        blank=True,
                                        null=True,
                                        verbose_name='Начало обеда')
    start_time_lunch = models.CharField(max_length=50,
                                        blank=True,
                                        null=True,
                                        verbose_name='Конец обеда')
    end_time_lunch = models.CharField(max_length=50,
                                      blank=True,
                                      null=True,
                                      verbose_name='Конец рабочего дня')
    text = models.TextField(blank=True,
                            null=True,
                            verbose_name='Текст')

    def __str__(self):
        return 'Режим работы архива'


class Link(models.Model):
    """
    Ссылки, по типу ссылки
    """
    name = models.CharField(max_length=250,
                            verbose_name='Название')
    slug = models.SlugField(max_length=250)
    type_link = models.CharField(max_length=250,
                                 verbose_name='Тип ссылки')
    url = models.URLField(verbose_name='Адрес ссылки',
                          default=None)

    def __str__(self):
        return f'Сслыка на {self.name}'


class ListBooks(models.Model):
    numb = models.IntegerField(verbose_name='Порядковый номер')
    author = models.CharField(max_length=255,
                              verbose_name='Автор книги')
    name = models.CharField(max_length=255,
                            verbose_name='Название книги')
    slug = models.SlugField(max_length=255)
    publishing = models.CharField(max_length=255,
                                  verbose_name='Издательство')

    class Meta:
        ordering = ['numb']

    def __str__(self):
        return f'Книга из чит. зала номер {self.numb}'


class ImageForPost(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='images')
    image = models.ImageField(blank=True,
                              null=True,
                              upload_to='archive',
                              verbose_name='Изображение')


