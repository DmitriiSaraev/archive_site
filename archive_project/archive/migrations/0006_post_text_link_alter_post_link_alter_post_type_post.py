# Generated by Django 4.2 on 2024-05-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0005_imageforpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_link',
            field=models.CharField(default='text', max_length=200, verbose_name='Текст ссылки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес ссылки'),
        ),
        migrations.AlterField(
            model_name='post',
            name='type_post',
            field=models.CharField(choices=[('main_them', 'Основной пост на главной'), ('about_archive', 'Об архиве'), ('news', 'Новости'), ('article', 'Статьи'), ('exhibitions', 'Выставки'), ('reading_room', 'Читальный зал'), ('requests_ls', 'запросы тематические'), ('requests_sp', 'запросы соц. пр.'), ('external_reference', 'внешние ссылки')], max_length=100, verbose_name='Тип поста'),
        ),
    ]
