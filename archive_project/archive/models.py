from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


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
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

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

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

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

    class Meta:
        verbose_name = 'Режим работы'
        verbose_name_plural = 'Режимы работы'

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

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

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
        verbose_name = 'Список книг'
        verbose_name_plural = 'Списки книг'

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

    class Meta:
        verbose_name = 'Фото для поста'
        verbose_name_plural = 'Фотографии для поста'

    def save(self, *args, **kwargs):
        if self.image:
            max_width = 700
            max_height = 520

            # Открыть изображение с помощью Pillow
            img = Image.open(self.image)

            # Подгонка размера изображения
            img.thumbnail((max_width, max_height), Image.LANCZOS)

            # Получение новых размеров изображения
            width, height = img.size

            # Заполнение недостающих областей фоном
            background = Image.new('RGB', (max_width, max_height),
                                   (255, 255, 255))
            offset = ((max_width - width) // 2, (max_height - height) // 2)
            background.paste(img, offset)

            # Сохранение обработанного изображения
            img_io = BytesIO()
            background.save(img_io, format='JPEG')
            self.image.file = InMemoryUploadedFile(
                img_io, None, self.image.name, 'image/jpeg', img_io.tell(),
                None
            )

        super().save(*args, **kwargs)

# @receiver(pre_save, sender=ImageForPost)
# def process_image(sender, instance, **kwargs):
#     image = instance.image
#     max_width = 700
#     max_height = 520
#
#     # Открыть изображение с помощью Pillow
#     img = Image.open(image)
#
#     # Подгонка размера изображения
#     img.thumbnail((max_width, max_height), Image.LANCZOS)
#
#     # Получение новых размеров изображения
#     width, height = img.size
#
#     # Заполнение недостающих областей фоном
#     background = Image.new('RGB', (max_width, max_height), (255, 255, 255))
#     offset = ((max_width - width) // 2, (max_height - height) // 2)
#     background.paste(img, offset)
#
#     # Сохранение обработанного изображения
#     img_io = BytesIO()
#     background.save(img_io, format='JPEG')
#     image.file = InMemoryUploadedFile(
#         img_io, None, instance.image.name, 'image/jpeg', img_io.tell(), None
#     )
