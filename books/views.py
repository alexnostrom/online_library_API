from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .custom_permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
	try:
		data = request.data
		user = User.objects.create(
			username=data['username'],
			first_name=data['firstname'],
			last_name=data['lastname'],
			password=make_password(data['password'])
		)
		serializer = UserSerializerToken(user, many=False)
		return Response(serializer.data)
	except Exception as e:
		error_message = e.args[0]
		message = {
			"status": 'error',
			'message': error_message
		}
		return Response(message, status=status.HTTP_400_BAD_REQUEST)


class AddBookOrGetAllBooksViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsAdminOrReadOnly)


class BookAPIDetailViewSet(viewsets.ModelViewSet):
	serializer_class = BookDetailSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsAdminOrReadOnly)

	def get_queryset(self):
		pk = self.kwargs.get('pk')
		return Book.objects.filter(pk=pk)


class AuthorsAPIViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
	permission_classes = (IsAuthenticated, IsAdminOrReadOnly)


class ReviewAPIDeleteViewSet(generics.DestroyAPIView, generics.ListAPIView):
	serializer_class = ReviewSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsAdminOrReadOnly)

	def get_queryset(self):
		book_id = self.kwargs['book_id']
		pk = self.kwargs['pk']
		return Review.objects.filter(pk=pk, book_id=book_id)


class ReviewCreate(generics.CreateAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsAdminOrReadOnly)

	def perform_create(self, serializer):
		book = get_object_or_404(Book, pk=self.kwargs['book_id'])
		serializer.save(book=book)
