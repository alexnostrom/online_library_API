from rest_framework import serializers
from .models import Book, Author, Review


class BookSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Book
		fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Author
		fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Review
		fields = "__all__"
