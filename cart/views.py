from django.shortcuts import render, redirect

# Create your views here.
def view_cart(request):
     return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('cart', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['cart'] = bag
    print(request.session['cart'])
    return redirect(redirect_url)




    
    
   