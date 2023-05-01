from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart currently")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MzNKpBmLoLbFeg9C5XhIR5FiviBvmdyoqYvifZlkC8uOHZjd4VLyTpnT1hJsIm42lljHpYW30TXopgfLWnpsJoI00FyTPDbR8',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
