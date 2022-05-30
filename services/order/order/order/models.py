import time
import decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from order.core.behaviours import StatusMixin
from order.core.models import Address


class OrderStatus(models.TextChoices):
    PLACED = 'PL', _('PLACED')
    PROCESSING = 'PR', _('PROCESSING')
    ON_THE_WAY = 'OW', _('ON_THE_WAY')
    OUT_FOR_DELIVERY = 'OD', _('OUT_FOR_DELIVERY')
    DELIVERED = 'DL', _('DELIVERED')
    RETURN = 'RT', _('RETURN')
    FAILED = 'FL', _('FAILED')
    CANCELLED = 'CL', _('CANCELLED')
    EXCHANGE = 'EX', _('EXCHANGE')


class Order(StatusMixin, TimeStampedModel):
    order_number = models.CharField(_('Order Number'), max_length=100, blank=True, null=True)
    customer = models.BigIntegerField(_('Customer'), blank=True, null=True)
    payment = models.BigIntegerField(_('Payment'), blank=True, null=True)
    tax_amount = models.DecimalField(_('Tax Amount'), max_digits=100, decimal_places=2, blank=True, null=True)
    shipping_amount = models.DecimalField(_('Shipping Amount'), max_digits=100, decimal_places=2, blank=True,
                                          null=True, default=0)
    total_amount = models.DecimalField(_('Total Amount'), max_digits=100, decimal_places=2, blank=True, null=True)

    status = models.CharField(_('Order Status'), max_length=2, choices=OrderStatus.choices,
                              default=OrderStatus.PLACED, blank=True, null=True)
    delivered_at = models.DateTimeField(_('Delivered At'), auto_now_add=False, blank=True, null=True)
    shipping_address = models.ForeignKey('core.Address', on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.order_number = '-'.join([str(self.customer)] + str(time.time()).split('.'))

        self.total_amount = self.shipping_amount + self.tax_amount
        for order_item in OrderItem.objects.filter(order=self.id):
            self.total_amount += order_item.quantity * order_item.price
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f'Order #{self.order_number}'


class OrderItem(StatusMixin, TimeStampedModel):
    product = models.BigIntegerField(_('Product'), blank=True, null=True)
    quantity = models.IntegerField(_('Quantity'), blank=True, null=True)
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=7, blank=True, null=True)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, blank=True, null=True,
                              related_name='order_items')

    def __str__(self):
        return f'Order #{self.order.order_number} - {self.product}'
