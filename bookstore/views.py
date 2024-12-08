from django.shortcuts import render, redirect
from django.urls import reverse
from item.models import Category, Item
from .forms import SignupForm

def index(request):
    """
    View to render the home page with categories and the latest items.
    """
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    
    return render(request, 'bookstore/index.html', {
        'categories': categories,
        'items': items,
    })  

def contact(request):
    """
    View to render the contact page.
    """
    return render(request, 'bookstore/contact.html')

def signup(request):
    """
    View to handle user signup with the SignupForm.
    Redirects to the login page on successful signup.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            # Redirect to login page after successful signup
            return redirect(reverse('bookstore:login'))
    else:
        form = SignupForm()

    return render(request, 'bookstore/signup.html', {
        'form': form
    })
