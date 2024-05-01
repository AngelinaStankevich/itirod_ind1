from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from cart.forms import CartAddProductForm
from .models import Profile, Photo, Comment


def index(request):
    profiles = Profile.objects.all()
    return render(request, 'portfolio/index.html', {'profiles': profiles})


def profile_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    photos = Photo.objects.filter(profile=profile)
    cart_product_form = CartAddProductForm()  # Здесь необходимо создать форму для добавления в корзину, если она используется
    return render(request, 'portfolio/profile_detail.html', {'profile': profile, 'photos': photos, 'cart_product_form': cart_product_form})


@login_required
def add_comment(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        text = request.POST.get('comment_text')
        Comment.objects.create(photo=photo, user=request.user, text=text)
    return redirect('photo_detail', photo_id=photo_id)

