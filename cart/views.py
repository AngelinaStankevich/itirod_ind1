from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from portfolio.models import Profile
from .forms import CartAddProductForm


@require_POST
def cart_add(request, profile_id):
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = cd.get('quantity', 1)  # Default quantity to 1 if 'quantity' is missing
        cart.add(profile_id=profile_id, quantity=quantity)
    return redirect('cart:cart_detail')


def cart_remove(request, profile_id):
    cart = Cart(request)
    cart.remove(profile_id)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    profile_ids = cart.get_profiles()  # Получаем список ID профилей из корзины
    profiles = Profile.objects.filter(id__in=profile_ids)  # Получаем соответствующие профили
    profile_photos = {}
    for profile in profiles:
        profile_photos[profile.id] = profile.photo.url if profile.photo else None

    return render(request, 'cart/cart_detail.html',
                  {'profiles': profiles, 'profile_photos': profile_photos, 'cart': cart})
