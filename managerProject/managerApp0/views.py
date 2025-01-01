from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import BookForm
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()  # Récupérer tous les livres
    return render(request, 'managerApp0/book_list.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)  # Récupérer un livre par son ID
    return render(request, 'managerApp0/book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistrer le livre
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'managerApp0/book_form.html', {'form': form})

def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'managerApp0/book_form.html', {'form': form})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'myapp/book_confirm_delete.html', {'book': book})


