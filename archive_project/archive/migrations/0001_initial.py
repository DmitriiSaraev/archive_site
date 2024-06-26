# Generated by Django 4.2 on 2024-05-04 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('address', models.TextField()),
                ('boss', models.CharField(max_length=100)),
                ('senior_archivist', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('type_link', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ListBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numb', models.IntegerField()),
                ('author', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('publishing', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('name_day', models.CharField(blank=True, max_length=50, null=True)),
                ('start_time_morning', models.CharField(blank=True, max_length=50, null=True)),
                ('end_time_morning', models.CharField(blank=True, max_length=50, null=True)),
                ('start_time_lunch', models.CharField(blank=True, max_length=50, null=True)),
                ('end_time_lunch', models.CharField(blank=True, max_length=50, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('type_post', models.CharField(choices=[('main_them', 'Основной пост на главной'), ('about_archive', 'Об архиве'), ('news', 'Новости'), ('article', 'Статьи'), ('exhibitions', 'Выставки'), ('reading_room', 'Читальный зал'), ('requests_ls', 'запросы л/с'), ('requests_sp', 'запросы соц. пр.')], max_length=100)),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='archive')),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
