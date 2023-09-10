from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
	firstname = models.CharField(max_length=50, verbose_name='Имя')
	lastname = models.CharField(max_length=100, verbose_name='Фамилия')
	biography = models.TextField(blank=True, verbose_name='Биография')

	class Meta:
		verbose_name = 'Автор'
		verbose_name_plural = 'Авторы'

	def __str__(self):
		return f"{self.firstname} {self.lastname}"


class Book(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название')
	description = models.TextField(blank=True, verbose_name='Описание')
	publish_date = models.IntegerField(verbose_name='Дата публикации')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book_author = models.ForeignKey(Author, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'
		ordering = ['-publish_date']

	def __str__(self):
		return f"{self.title}"


class Review(models.Model):
	content = models.TextField(max_length=500, verbose_name='Отзыв')
	rating = models.IntegerField(verbose_name='Рейтинг')
	review_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
	book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.PROTECT)

	class Meta:
		verbose_name = 'Описание'
		verbose_name_plural = 'Описание'
		ordering = ['rating']

	def __str__(self):
		return f"{self.content} {self.rating}"
