from django.urls import path
from .views import home, shop, cart

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
]
