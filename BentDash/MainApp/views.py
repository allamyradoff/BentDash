from django.shortcuts import render, redirect
from MainApp.models import *
from .forms import ContactUsForm
import random


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    stars = Stars.objects.all()
    banners = Banner.objects.all()
    contact = Contact.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "stars": stars,
        "banners": banners,
        "contact":contact
    }
    return render(request, 'index.html', context)


def category(request, slug):
    categories = Category.objects.all()
    products = Product.objects.filter(category__slug=slug)
    stars = Stars.objects.all()
    banners = Banner.objects.all()
    contact = Contact.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "stars": stars,
        "contact":contact,
        "banners": banners,
    }
    return render(request, 'category.html', context)


def product(request, slug):
    products = Product.objects.filter(category__slug=slug)
    categories = Category.objects.all()
    contact = Contact.objects.all()
    banners = ProductBanner.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "banners": banners,
        "contact":contact,
    }
    return render(request, 'product.html', context)


def product_all(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    banners = ProductBanner.objects.all()
    contact = Contact.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "banners": banners,
        "contact":contact,
    }
    return render(request, 'product_all.html', context)


def about_us(request):
    about = AboutUs.objects.all()
    categories = Category.objects.all()
    contact = Contact.objects.all()
    context = {
        "categories": categories,
        "about": about,
        "contact":contact,
    }
    return render(request, 'about.html', context)

def contact(request):
    contact = Contact.objects.all()
    about = AboutUs.objects.all()

    form = ContactUsForm()
    if request.method=="POST":
        form=ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "contact": contact,
        "form":form,
        "about": about,

    }
    return render(request, 'contact.html', context)



def product_single(request, slug, id):
    categories = Category.objects.all()
    products = Product.objects.filter(slug=slug)
    contact = Contact.objects.all()
    last = Product.objects.filter(id=id)


    context = {
        "products": products,
        "contact":contact,
        "last":last,
        "categories": categories,
    }
    return render(request, 'single-product.html', context)

