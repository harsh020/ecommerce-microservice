from django.contrib import admin

from payment.payment.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    model = Payment
