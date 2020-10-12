from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from authapp.models import ShopUser
from django.urls import reverse
from mainapp.models import ProductCategory

from mainapp.models import Product

from adminapp.forms import ShopUserAdminEditForm

from adminapp.forms import ProductCategoryEditForm


@user_passes_test(lambda u:u.is_superuser)
def user_create(request):
    title = 'Пользователь/создание'

    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserAdminEditForm()


    content = {
        'title': title,
        'update_form': user_form
    }
    return render (request, 'adminapp/users_update.html', content)

@user_passes_test(lambda u:u.is_superuser)
def users(request):
    title = 'Пользователи'

    users_list = ShopUser.objects.all()

    content = {
        'title': title,
        'objects': users_list,
    }
    return render(request, 'adminapp/users.html', content)

@user_passes_test(lambda u:u.is_superuser)
def user_update(request, pk):
    title = 'Пользователь/редактирование'

    edit_user = get_object_or_404 (ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserAdminEditForm (request.POST, request.FILES, instance=edit_user)
        if user_form.is_valid ():
            user_form.save ()
            return HttpResponseRedirect (reverse ('admin:users', argw=[edit_user.pk]))
    else:
        user_form = ShopUserAdminEditForm (instance=edit_user)

        content = {
            'title': title,
            'update_form': user_form
        }
        return render (request, 'adminapp/users_update.html', content)

@user_passes_test(lambda u:u.is_superuser)
def user_delete(request, pk):
    title = 'Пользователь/удаление'

    edit_user = get_object_or_404 (ShopUser, pk=pk)
    if request.method == 'POST':
        edit_user.delete()
        return HttpResponseRedirect(reverse('admin:users'))
    content = {
            'title': title,
            'user_to_delete': edit_user
        }
    return render (request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u:u.is_superuser)
def category_create(request, pk):
    title = 'категории/создание'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm (request.POST, request.FILES)
        if category_form.is_valid ():
            category_form.save ()
            return HttpResponseRedirect (reverse ('admin:categories'))
    else:
        category_form = ProductCategoryEditForm ()

    content = {
            'title': title,
            'update_form': category_form
        }
    return render (request, 'adminapp/category_update.html', content)

@user_passes_test(lambda u:u.is_superuser)
def categories(request):
    title = 'Категории'
    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u:u.is_superuser)
def category_update(request, pk):
    title = 'категории/редактирование'
    category_item = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category_form = ProductCategoryEditForm (request.POST, request.FILES, instance=category_item)
        if category_form.is_valid ():
            category_form.save ()
            return HttpResponseRedirect (reverse ('admin:categoty_update,', args=[category_item.pk]))
    else:
        category_form = ProductCategoryEditForm (instance=category_item )

    content = {
        'title': title,
        'update_form': category_form
    }
    return render (request, 'adminapp/category_update.html', content)

@user_passes_test(lambda u:u.is_superuser)
def category_delete(request, pk):
    title = 'категории/удаление'

    category_item = get_object_or_404 (ProductCategory, pk=pk)
    if request.method == 'POST':
        category_item.is_active= False
        category_item.save()
        return HttpResponseRedirect (reverse ('admin:categories'))
    content = {
        'title': title,
        'category_to_delete': category_item
    }
    return render (request, 'adminapp/category_delete.html', content)


@user_passes_test(lambda u:u.is_superuser)
def product_create(request, pk):
    pass

@user_passes_test(lambda u:u.is_superuser)
def products(request, pk):
    title = 'Продукты'
    categories_item = get_object_or_404(ProductCategory,pk=pk)
    products_list = Product.objects.filter(category=categories_item)
    content = {
        'title': title,
        'objects': products_list,
        'category': categories_item
    }
    return render (request, 'adminapp/categories.html', content)

@user_passes_test(lambda u:u.is_superuser)
def product(request, pk):
    pass

@user_passes_test(lambda u:u.is_superuser)
def product_update(request, pk):
    pass

@user_passes_test(lambda u:u.is_superuser)
def product_delete(request, pk):
    pass