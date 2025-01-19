from django.urls import path
from .views import EventStoreHome, EventStoreAbout, EventStoreContact, EventStoreEventDetail, EventStoreSearch, EventStoreShopCart, EventStoreUserOrders, EventStoreListByTag
from django.conf.urls.static import static
from django.conf import settings

app_name = 'event_store'
urlpatterns = [
    path('', EventStoreHome, name='EventStoreHome'),
    path('tag/<slug:tag>/', EventStoreListByTag, name='EventStoreListByTag'),
    path('event/<int:event_id>/', EventStoreEventDetail, name='EventStoreEventDetail'),
    path('about/', EventStoreAbout, name='EventStoreAbout'),
    path('contact/', EventStoreContact, name='EventStoreContact'),
    path('search/', EventStoreSearch, name='EventStoreSearch'),
    path('shopcart/', EventStoreShopCart, name='EventStoreShopCart'),
    path('userorder/', EventStoreUserOrders, name='EventStoreUserOrders'),
]