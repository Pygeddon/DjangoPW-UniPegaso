from django.urls import path
from .views import EventManagerHome, EventManagerCreateEvent, EventManagerDeleteOrder, EventManagerModifyEvent, EventManagerDeleteEvent, EventManagerModifyOrder, EventManagerAddDatesToEvent

app_name = 'event_manager'

urlpatterns = [ 
    path('', EventManagerHome, name='EventManagerHome'),
    path('create_event/', EventManagerCreateEvent, name='EventManagerCreateEvent'),
    path('modify_event/<int:event_id>/', EventManagerModifyEvent, name='EventManagerModifyEvent'),
    path('delete_event/<int:event_id>/', EventManagerDeleteEvent, name='EventManagerDeleteEvent'),
    path('add_dates_to_event/<int:event_id>/', EventManagerAddDatesToEvent, name='EventManagerAddDatesToEvent'),
    path('modify_order/<int:order_id>/', EventManagerModifyOrder, name='EventManagerModifyOrder'),
    path('delete_order/<int:order_id>', EventManagerDeleteOrder, name='EventManagerDeleteOrder'),
]