from django.urls import path
from .views import EventShopBuyTicket, EventShopBuyTicketStep2, EventShopCreateOrder
from django.conf import settings
from django.conf.urls.static import static

app_name = 'event_shop'
urlpatterns = [ 
    path('', EventShopBuyTicket, name='EventShopBuyTicket'),
    path('buyticket/', EventShopBuyTicketStep2, name='EventShopBuyTicketStep2'),
    path('createorder/', EventShopCreateOrder, name='EventShopCreateOrder')
]