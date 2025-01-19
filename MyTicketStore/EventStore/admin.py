from django.contrib import admin

from EventManager.models import Event, EventDates, Order, EventTags
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('name', 'location', 'ticket_Intero_cost', 'ticket_Ridotto_cost', 'ticket_Gruppo_cost', 'tag_list')
    search_fields = ('name', 'location')
    list_filter = ('name','location')
    ordering = ('name', 'location', 'ticket_Intero_cost', 'ticket_Ridotto_cost', 'ticket_Gruppo_cost')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

class EventDatesAdmin(admin.ModelAdmin):
    model = EventDates
    list_display = ('date', 'event', 'tickets_available', 'created', 'modified')
    search_fields = ('date', 'event')
    list_filter = ('date','event')
    ordering = ('date', 'event', 'tickets_available')

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('event', 'date', 'user', 'num_tickets_interi', 'num_tickets_ridotti', 'num_tickets_gruppi', 'total', 'created', 'modified')
    search_fields = ('event', 'date', 'user')
    list_filter = ('event','user')
    ordering = ('event', 'date', 'user')

admin.site.register(Event, EventAdmin)
admin.site.register(EventDates, EventDatesAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(EventTags)