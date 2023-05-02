from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Orders

def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form':form,
        
    }

    return render(request, template, context)

    def order_pasty(request, order_id):
     order = get_object_or_404(Order, order_id=order_id)

    messages.info(request, (
        f'This is a past confirmation for order ID {order_id}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

