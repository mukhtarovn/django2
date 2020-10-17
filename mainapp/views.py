import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from mainapp.models import *

# Create your views here.
from mainapp.models import Product, ProductCategory

from basketapp.models import Basket

links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классик'},
    ]
def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products_list = Product.objects.all()
    return random.sample(list(products_list), 1)[0]

def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category_id).\
                                    exclude(pk=hot_product.pk)[:3]

    return same_products



def main(request):
    title = 'продукты'
    content = {
        'title': title
    }
    return render(request, 'mainapp/index.html', content)

def products (request, pk=None, page=1):

    links_menu = ProductCategory.objects.all()
    title = 'продукты'


    if pk is not None:
        if pk == 0:
            products = Product.objects.all()
            category = {
                'pk': 0,
                'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk= pk)
            products = Product.objects.filter(category=category).order_by('-price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page (paginator.num_pages)
        content = {
            'links_menu': links_menu,
            'title': title,
            'category': category,
            'products': products_paginator,
            'basket': get_basket(request.user)
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {
        'links_menu': links_menu,
        'title': title,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/products.html', content)

def contact (request):
    title = 'контакты'
    content = {
        'title': title, 'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/contact.html', content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all (),
        'product': get_object_or_404 (Product, pk=pk),
        'basket': get_basket (request.user),
    }

    return render (request, 'mainapp/product.html', content)
