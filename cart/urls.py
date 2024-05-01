from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('detail/', views.cart_detail, name='cart_detail'), # Страница с содержимым корзины
    path('add/<int:profile_id>/', views.cart_add, name='cart_add'),  # Добавление профиля в корзину
    path('remove/<int:profile_id>/', views.cart_remove, name='cart_remove'),  # Удаление профиля из корзины
]
