# Generated by Django 5.1.7 on 2025-03-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_bookcategory_slug_ebook_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='views',
            field=models.PositiveBigIntegerField(default=0, help_text='views for book', verbose_name='views'),
        ),
    ]
