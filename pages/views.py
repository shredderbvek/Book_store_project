from django.shortcuts import render, get_object_or_404, redirect
from book_listings.models import Book
from django.core.mail import send_mail
from django.urls import reverse
from newsletter.models import NewsletterSubscriber
from django.db import IntegrityError
from django.contrib import messages


def index(request):
    new_arrivals = Book.objects.order_by('-date_added')[:4]
    pick_of_the_week = get_object_or_404(Book, pick_of_the_week=True)
    best_sellers = Book.objects.filter(best_seller=True).order_by('title')
    context = {
        'new_arrivals': new_arrivals,
        'pick_of_the_week': pick_of_the_week,
        'best_sellers': best_sellers,
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        try:
            new_subscriber = NewsletterSubscriber(name=name, email=email)
            new_subscriber.save()
        except IntegrityError:
            messages.error(request, ': Email is already subscribed to the newsletter')
            return render(request, 'pages/index.html', context)
        else:
            send_mail(
                'Newsletter Subscription',
                f'Dear {name},\n Thank you for subscribing to our newsletter.\nWith regards,\nHamro Pustakalaya',
                'ghostrobot96@gmail.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, ': Thank you for subscribing to our newsletter')
            return redirect(reverse('index'))
    else:
        return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        full_name = request.POST['full-name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            f'from: {full_name}\n email: {email} \n message: \n {message}',
            'ghostrobot96@gmail.com',
            ['shredderbvek@gmail.com'],
            fail_silently=False,
        )
        return redirect(reverse('contact'))
    else:
        return render(request, 'pages/contact.html')
