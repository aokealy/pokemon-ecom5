from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):

    products = Product.objects.all()

    if request.GET:
        if 'q' in request.GET:
            inquire = request.GET['q']
            if not inquire:
                messages.error(request, "please enter a valid search")
                return redirect(reverse('products'))


    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
