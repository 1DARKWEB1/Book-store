from django.shortcuts import render, redirect, HttpResponse

from book.forms import CategoryForm, BookForm
from book.models import Book, Category


def index(request):
    books = Book.objects.all()
    category = Category.objects.all()

    return render(request, 'book/index.html', {'books': books, 'category': category})


def book_lists(request):
    books = Book.objects.all()
    category = Category.objects.all()

    return render(request, 'book/book_lists.html', {'books': books, 'category': category})


def admin(request):
    authenticated = False

    user = {
        'username': 'admin',
        'password': '1234'
    }

    if request.method == "POST":
        if user['username'] == request.POST['username'] and user['password'] == request.POST['password']:
            authenticated = True
        else:
            warning = "Wrong password"
            return render(request, 'book/login.html', {'error': warning})
    if authenticated:
        category_form = CategoryForm()
        book_form = BookForm()
        category_list = Category.objects.all()
        book_list = Book.objects.all()
        return render(request, 'book/admin-page.html', {
            "category_form": category_form,
            "book_form": book_form,
            "category_list": category_list,
            "book_list": book_list,
        })
    else:
        return render(request, 'book/login.html')


def admin_list(request):
    book = Book.objects.all()
    book_form = BookForm()
    return render(request, 'book/admin-lists.html', {'book': book, 'book_form': book_form})


def books(request):
    book = Book.objects.all()
    return render(request, 'book/book_lists.html', {'books': book})


def directions(request, pk):
    book = Book.objects.filter(category=pk)
    book_pdf = Book.objects.all()
    if book:
        return render(request, 'book/book_lists.html', {'books': book})
    else:
        test = "NOT FOUND"
        return render(request, 'book/book_lists.html', {'test': test})


def admin_sort(request, pk):
    book = Book.objects.filter(category=pk)
    book_pdf = Book.objects.all()
    if book:
        return render(request, 'book/admin-lists.html', {'book': book})
    else:
        test = "NOT FOUND"
        return render(request, 'book/admin-lists.html', {'test': test})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin-page/')
        else:
            return redirect('/admin-page/')


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin-lists/')
        else:
            print(form.errors)
            return redirect('/admin-lists/')


def delete_category(request, pk):
    if request.method == "POST":
        cat = Category.objects.get(id=pk)
        book = Book.objects.all()
        cat.delete()
        book.delete()

        return redirect('/admin-page/')


def delete_book(request, pk):
    if request.method == "POST":
        book = Book.objects.get(id=pk)
        book.delete()

        return redirect('/admin-lists/')
