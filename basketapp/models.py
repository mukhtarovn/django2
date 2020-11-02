from django.conf import settings
from django.db import models

# Create your models here.

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    add_datetime = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity (self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x:x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost (self):
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x:x.product_cost, _items)))
        return _total_cost

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category')

    @staticmethod
    def get_product (user,product):
        return Basket.objects.filter(user=user, product=product)

    @classmethod
    def get_product_quantity(cls, user):
        basket_items = cls.get_items(user)
        basket_items_dic = {}
        [basket_items_dic.update({item.product: item.quantity}) for item in basket_items]

        return basket_items_dic

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - \
                                     self.__class__.get_item (self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save ()
        super (self.__class__, self).save (*args, **kwargs)


