from django.shortcuts import get_object_or_404, render
from django.db.models import Avg

from .models import Book


# Create your views here.
def index(request):
    # order by db column with '-' is discending order
    books = Book.objects.all().order_by("-title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))  # rating__avg

    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_number_of_books": num_books,
            "average_rating": avg_rating,
        },
    )


def book_detail(request, slug):

    book = get_object_or_404(Book, slug=slug)

    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestselling,
        },
    )
