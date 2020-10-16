from django.db import models
from datetime import datetime
from .categories import category_choice


class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fb_url = models.URLField(verbose_name='facebook URL', blank=True)
    insta_url = models.URLField(verbose_name='instagram URL', blank=True)
    twitter_url = models.URLField(verbose_name='twitter URL',  blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    web_url = models.URLField()

    def __str__(self):
        return self.name


class Book(models.Model):
    GENRE_CHOICE = category_choice
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    isbn = models.BigIntegerField()
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100)
    size = models.CharField(max_length=20, blank=True, help_text='Please use the following format: <em>l*b mm</em>.')
    pages = models.IntegerField(blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(default=datetime.now)
    best_seller = models.BooleanField(default=False)
    pick_of_the_week = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
