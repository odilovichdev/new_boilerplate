from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.db import models

from apps.common.models import BaseModel

Users = get_user_model()


class Cart(BaseModel):
    count = models.IntegerField(_("Count"))
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return f"{self.user_id | self.book_id}"

class Order(BaseModel):
    class OrderStatus(models.TextChoices):
        BOUGHT = 'bought'
        CANCELED = 'canceled'
        DELIVERED = 'delivered'

    order_number = models.IntegerField(_("Order Number"), unique=True)
    total_price = models.DecimalField(_("Total Price"), max_digits=10, decimal_places=2)
    status = models.CharField(_("Status"), max_length=20, choices=OrderStatus.choices)
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.user_id}"


class OrderItem(BaseModel):
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.book_id | self.order_id}"



