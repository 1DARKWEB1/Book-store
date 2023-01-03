from django.urls import path

from book.views import index, admin, add_category, add_book, delete_category, delete_book, admin_list, book_lists, directions,admin_sort

urlpatterns = [
    path('', index, name="index"),
    path('admin-page/', admin, name="admin"),
    path('admin-lists/', admin_list, name="lists"),
    path('book-lists/', book_lists, name='books'),
    path('directions/<int:pk>/', directions),
    path('admin_sort/<int:pk>/', admin_sort),
    path('add-category/', add_category),
    path('add-book/', add_book),
    path('delete-book/<int:pk>/', delete_book),
    path('delete-category/<int:pk>/', delete_category),
]
