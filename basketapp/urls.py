import basketapp.views as basketapp
from django.urls import path

app_name='basketapp'

urlpatterns = [
    path('', basketapp.basket, name='basket'),
    path('add/<pk>/', basketapp.basket_add, name='add'),
    path('remove/<pk>/', basketapp.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit')
]
