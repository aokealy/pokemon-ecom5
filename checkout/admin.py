from django.contrib import admin
from .models import Orders, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrdersAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_id', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_id', 'date', 'first_name', 'last_name', 'email', 'phone', 'country', 'zipcode', 'city', 'street_address1',
              'street_address2', 'county', 'delivery_cost', 'order_total', 'grand_total',)

    list_display = ('order_id', 'date', 'first_name', 'last_name', 'order_total', 'delivery_cost', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Orders, OrdersAdmin)