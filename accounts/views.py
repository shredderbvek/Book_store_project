from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from accounts.models import UserInquiry


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                messages.success(request, ': Login successful!!')
                return redirect(reverse('dashboard'))
            else:
                messages.error(request, ': The account is not active anymore. Please register a new account')
                return redirect(reverse('register'))
        else:
            messages.error(request, ': Please enter a valid username and password')
            return redirect(reverse('login'))
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm-password']

        if password == password2:
            if not User.objects.filter(username=username):
                if not User.objects.filter(email=email):
                    new_user = User.objects.create_user(username=username, email=email, password=password)
                    new_user.first_name = first_name
                    new_user.last_name = last_name
                    new_user.save()
                    messages.success(request, ': You are now registered and can login')
                    return redirect(reverse('login'))
                else:
                    messages.error(request, ': Email already exists')
                    return redirect(reverse('register'))
            else:
                messages.error(request, ': Username already exists')
                return redirect(reverse('register'))
        else:
            messages.error(request, ': Passwords don\'t match')
            return redirect(reverse('register'))
    else:
        return render(request, 'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    user_inquiries = UserInquiry.objects.all().order_by('-inquiry_date')
    context = {
        'user_inquiries': user_inquiries,
    }
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    messages.success(request, ': You have been successfully logged out')
    auth.logout(request)
    return redirect(reverse('index'))
