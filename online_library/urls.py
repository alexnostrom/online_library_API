"""
URL configuration for online_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import AddBookOrGetAllBooksViewSet, AuthorsAPIViewSet, BookAPIDetailViewSet, registerUser, \
	MyTokenObtainPairView, ReviewAPIDeleteViewSet, ReviewCreate

urlpatterns = [
	path('admin/', admin.site.urls),
	path('register/', view=registerUser, name='register'),
	path('login/', view=MyTokenObtainPairView.as_view(), name='login'),
	path('books/', AddBookOrGetAllBooksViewSet.as_view({'get': 'list', 'post': 'create'}), name='books'),
	path('books/<int:pk>/', BookAPIDetailViewSet.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy'})),
	path('authors/', AuthorsAPIViewSet.as_view({'get': 'list'}), name='authors'),
	path('books/<int:book_id>/review/<int:pk>/', ReviewAPIDeleteViewSet.as_view()),
	path('books/<int:book_id>/review/', ReviewCreate.as_view()),

]
