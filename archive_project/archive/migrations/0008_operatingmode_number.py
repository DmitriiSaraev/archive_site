# Generated by Django 4.2 on 2024-05-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0007_alter_post_text_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatingmode',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Порядковый номер дня'),
            preserve_default=False,
        ),
    ]
