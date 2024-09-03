from django.urls import path
from . import views

urlpatterns = [
    path('author/create/', views.author_create, name='author_create'),
    path('search/', views.search_books, name='search_books'),
]
