from django.db import models
from book_listings.models import Book
from django.contrib.auth.models import User
from datetime import datetime


class UserInquiry(models.Model):
    book_title = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    user_id = models.IntegerField()
    is_delivered = models.BooleanField(default=False)
    inquiry_date = models.DateTimeField(default=datetime.now)
