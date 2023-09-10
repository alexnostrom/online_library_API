from .serializers import BookSerializer, AuthorSerializer, ReviewSerializer
from .models import Book, Author, Review
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .custom_permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


# POST` /books/: Добавление новой книги
# d. `GET` /books/: Просмотр всех книг
class BookAPIList(generics.ListCreateAPIView):
	serializer_class = BookSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		pk = self.kwargs.get('pk')
		if not pk:
			return Book.objects.all()
		return Book.objects.filter(pk=pk)


# f. `PUT` /books/{book_id}: Редактирование книги
# g. `DELETE` /books/{book_id}: удаление книги
# e. `GET` /books/{book_id}: Получение детальной
# информации о книге.
class BookAPIDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = BookSerializer

	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsAdminOrReadOnly)

	def get_queryset(self):
		pk = self.kwargs.get('pk')
		if not pk:
			return Book.objects.all()
		return Book.objects.filter(pk=pk)


# GET` /authors/: Получение списка авторов
class AuthorsAPI(generics.ListAPIView):
	serializer_class = AuthorSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		pk = self.kwargs.get('pk')
		if not pk:
			return Author.objects.all()
		return Author.objects.filter(pk=pk)


# `POST` /books/{book_id}/review/: Добавление ревью к книге
# `DELETE` /books/{book_id}/review/: Удаление ревью

class ReviewAPI(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ReviewSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsAdminOrReadOnly)

	def get_queryset(self):
		pk = self.kwargs.get('pk')
		if not pk:
			return Review.objects.all()
		return Review.objects.filter(pk=pk)
