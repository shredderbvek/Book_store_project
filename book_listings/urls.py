from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_listings, name='bookListings'),
    path('<int:book_id>', views.book_listing, name='bookListing'),
    path('search', views.search, name='search'),
]