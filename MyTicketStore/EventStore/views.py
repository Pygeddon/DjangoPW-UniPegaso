from django.shortcuts import render
from EventManager.models import Event, EventDates,Order, EventTags
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

#Pagina di accesso al sito
def ProjectWorkWelcome(request):
    return render(request, 'projectwork_welcome.html')

#Homepage del sito, mostra gli eventi disponibili, i tag e la barra di ricerca
def EventStoreHome(request):
    events = Event.objects.all()
    tags = EventTags.objects.all()
    for event in events:
        logger.info(f'Event: {event.name}, Location: {event.location}')
    for event in events:
        first_date = EventDates.objects.filter(event=event).first()
        last_date = EventDates.objects.filter(event=event).last()
        event.first_date = first_date
        event.last_date = last_date
    context = {
        'events': events,
        'tags': tags,
    }
    return render(request, 'eventstore_home.html', context)

#Pagina che mostra tutti gli eventi, filtrati per un determinato tag
def EventStoreListByTag(request, tag):
    tags = EventTags.objects.all()
    print(tags)
    events = Event.objects.filter(tags__slug=tag)
    for event in events:
        first_date = EventDates.objects.filter(event=event).first()
        last_date = EventDates.objects.filter(event=event).last()
        event.first_date = first_date
        event.last_date = last_date
    context = {
        'events': events,
        'tags': tags
    }
    return render(request, 'eventstore_list_by_tag.html', context)

#Pagina che mostra i dettagli dell'evento selezionato

def EventStoreEventDetail(request, event_id):
    event = Event.objects.get(id=event_id)
    dates = EventDates.objects.filter(event=event)
    context = {
        'event': event,
        'dates': dates
    }
    return render(request, 'eventstore_detail.html', context)

#Pagina About Us, NON IMPLEMENTATA
def EventStoreAbout(request):
    return render(request, 'eventstore_about.html')

#Pagina di contatto, NON IMPLEMENTATA
def EventStoreContact(request):
    return render(request, 'eventstore_contact.html')

#Pagina di ricerca, permette di cercare eventi per nome o per luogo
def EventStoreSearch(request):
    if request.method == 'POST':
        if request.POST['search_event'] and not request.POST['search_by_location']:
            searched = request.POST['search_event']
            print(searched)
            events = Event.objects.filter(name__icontains= searched)
            context = {
                'events': events
            }
            return render(request, 'eventstore_search.html', context)
        if request.POST['search_by_location'] and not request.POST['search_event']:
            searched = request.POST['search_by_location']
            print(searched)
            events = Event.objects.filter(location__icontains= searched)
            context = {
                'events': events
            }
            return render(request, 'eventstore_search.html', context)
        
        if request.POST['search_event'] and request.POST['search_by_location']:
            searched_event = request.POST['search_event']
            searched_location = request.POST['search_by_location']
            events = Event.objects.filter(name__icontains= searched_event, location__icontains= searched_location)
            context = {
                'events': events
            }
            return render(request, 'eventstore_search.html', context    )
            
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'eventstore_search.html', context)

#Pagina del carrello, mostra gli ordini effettuati dall'utente
def EventStoreShopCart(request):
    if not request.session.is_empty():
        if request.session['event_id'] and request.session['date_id'] and request.session['tickets']:
            user = request.user
            event_id = request.session['event_id']
            date_id = request.session['date_id']
            tickets = request.session['tickets']
            total = tickets['totale']
            event = Event.objects.get(id=event_id)
            date = EventDates.objects.get(id=date_id)
            orders = Order.objects.filter(user=user, event=event, date=date)
            print(orders)
            context = {
                'orders': orders
            }
            return render(request, 'eventstore_shopping_cart.html', context)
        else:
            return render(request, 'eventstore_home.html')
    else:
        return render(request, 'eventstore_home.html')
    
#Pagina che mostra il dettaglio degli ordini effettuati dall'utente corrente del sito.
def EventStoreUserOrders(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    context = {
        'orders': orders
    }
    return render(request, 'eventstore_user_orders.html', context)
