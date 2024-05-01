from django.conf import settings
from portfolio.models import Profile


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = []
        self.cart = cart

    def add(self, profile_id, quantity=1, update_quantity=False):
        found = False
        for item in self.cart:
            if item['profile_id'] == profile_id:
                item['quantity'] += quantity
                found = True
                break
        if not found:
            self.cart.append({'profile_id': profile_id, 'quantity': quantity})
        self.save()

    def remove(self, profile_id):
        """
        Удаляем профиль из корзины
        """
        profile_id = str(profile_id)
        for item in self.cart:
            if item['profile_id'] == profile_id:
                self.cart.remove(item)
                break
        self.save()

    def save(self):
        # Обновляем сессию корзины
        self.session[settings.CART_SESSION_ID] = self.cart
        # Помечаем сессию как измененную
        self.session.modified = True

    def get_profiles(self):
        """
        Получаем все профили в корзине
        """
        profile_ids = [item['profile_id'] for item in self.cart]
        profiles = Profile.objects.filter(id__in=profile_ids)
        return profiles

    def clear(self):
        """
        Очищаем корзину
        """
        self.cart = []
        self.save()

    def __len__(self):
        """
        Подсчитываем общее количество профилей в корзине
        """
        return len(self.cart)
