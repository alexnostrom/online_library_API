# Generated by Django 4.2.5 on 2023-09-11 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_review_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='books.author', verbose_name='Автор книги'),
        ),
    ]
