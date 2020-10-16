from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Book
from accounts.models import UserInquiry
from django.contrib.auth.models import User
from .categories import genre
from django.core.paginator import Paginator
from django.core.mail import send_mail


def book_listings(request):
    books = Book.objects.filter(available=True).order_by('-date_added')
    paginator = Paginator(books, 12)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'books_listing': page_object,
        'genre': genre,
    }
    return render(request, 'book_listings/book_listings.html', context)


def book_listing(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {
        'book': book,
        'genre': genre,
    }
    if request.method == 'POST':
        book_title = request.POST['title']
        name = request.POST['full-name']
        email = request.POST['email']
        phone = request.POST['phone']
        delivery_address = request.POST['address']
        quantity = request.POST['quantity']
        if request.user.is_authenticated:
            user_id = request.POST['user_id']
            if User.objects.filter(id=user_id):
                new_inquiry = UserInquiry(book_title=book_title, user_id=user_id, quantity=quantity)
                new_inquiry.save()
        send_mail(
            'Book inquiry',
            f'Book: {book_title}\nname: {name}\nemail: {email}\nphone: {phone}\nquantity: {quantity}\naddress: {delivery_address}',
            'ghostrobot96@gmail.com',
            ['shredderbvek@gmail.com'],
            fail_silently=False,
        )
        return redirect(reverse('bookListing', args=[book_id]))
    return render(request, 'book_listings/book_listing.html', context)


def search(request):
    query_list = Book.objects.order_by('-date_added')
    if request.method == 'GET':
        if 'categories' in request.GET:
            categories = request.GET['categories']
            if categories:
                query_list = query_list.filter(genre__iexact=categories)
                
        if 'title' in request.GET:
            title = request.GET['title']
            if title:
                query_list = query_list.filter(title__iexact=title)

        if 'author' in request.GET:
            author = request.GET['author']
            if author:
                query_list = query_list.filter(author__name__iexact=author)

        if 'isbn' in request.GET:
            isbn = request.GET['isbn']
            if isbn:
                query_list = query_list.filter(isbn__iexact=isbn)

    context = {
        'genre': genre,
        'query_list': query_list,
        'values': request.GET,
    }
    return render(request, 'book_listings/search.html', context)
