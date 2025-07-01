#+ Handles the registration of a new user. This code is executed when the user submits the registration form.
#+
#+ It first checks if the passwords entered match, and then checks if the username or email already exists in the system. If either of these checks fail, it displays an error message and redirects the user back to the registration page.
#+
#+ If the checks pass, it creates a new user in the system with the provided username, password, email, first name, and last name. It then saves the user and displays a success message, redirecting the user to the login page.
#+


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from contact.models import Contact


# Login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'User logged in successfully')
            # Redirect to next if available, otherwise dashboard
            next_page = request.GET.get('next', 'dashboard')
            return redirect(next_page)
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')
# Register
def register(request):
    """
    Handles the registration of a new user. This code is executed when the user submits the registration form.
    It first checks if the passwords entered match, and then checks if the username or email already exists in the system. If either of these checks fail, it displays an error message and redirects the user back to the registration page.
    If the checks pass, it creates a new user in the system with the provided username, password, email, first name, and last name. It then saves the user and displays a success message, redirecting the user to the login page.
    """
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Check passwords match
        if password == password2:
            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'The email is already in use')
                return redirect('register')

            # Create user
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'accounts/register.html')

# Dashboard
@login_required(login_url='login')  # Ensures user is logged in
def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)

# Logout
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('index')
