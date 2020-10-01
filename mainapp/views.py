from django.shortcuts import render
from mainapp.models import ProductCategory

# Create your views here.
links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классик'},
    ]
def main(request):

    content = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', content)

def products (request, pk=None):
    print(pk)
    links_menu = ProductCategory.objects.all()
    content = {
        'links_menu': links_menu,
        'title': 'продукты',
    }
    return render(request, 'mainapp/products.html', content)

def contact (request):
    content = {
        'title': 'контакты',
    }
    return render(request, 'mainapp/contact.html', content)