from django import template

register = template.Library()

@register.filter(name='cal_subtotal')
def cal_subtotal(amount, quantity):
    return amount * quantity