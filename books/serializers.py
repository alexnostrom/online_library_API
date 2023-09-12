from .models import Book, Author, Review
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		data = super().validate(attrs=attrs)
		serializer = UserSerializerToken(self.user).data
		for k, v in serializer.items():
			data[k] = v

		return data


class UserSerializerToken(serializers.ModelSerializer):
	token = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'token')

	def get_token(self, object):
		token = RefreshToken.for_user(object)
		return str(token.access_token)


class AuthorSerializer(serializers.ModelSerializer):
	user = serializers.SlugRelatedField(slug_field="username", read_only=True)

	class Meta:
		model = Author
		fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
	"""Вывод отзыва"""
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Review
		fields = ('content', 'rating', 'user')


class BookSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Book
		fields = ('title', 'description', 'publish_date', 'book_author', 'user')


class BookDetailSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	reviews = ReviewSerializer(many=True, required=False)

	class Meta:
		model = Book
		fields = ('title', 'description', 'publish_date', 'book_author', 'user', 'reviews')
