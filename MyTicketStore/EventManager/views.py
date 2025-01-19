from django.shortcuts import get_object_or_404, render,HttpResponseRedirect
from EventManager.models import Event, EventDates, Order, EventTags
from EventManager.forms import CreateEventForm, ModifyEventForm, ModifyOrderForm, AddDatesToEventForm
from datetime import timedelta
from django.template.defaultfilters import slugify
from pathlib import Path
import boto3
from django.conf import settings
from django.contrib.auth.decorators import login_required
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

boto3.set_stream_logger('boto3.resources', logging.INFO)
BASE_DIR = Path(__file__).resolve().parent.parent


# Creo tutte le viste necessarie per l'applicazione EventManager

# Creo la vista per la home dell'EventManager
@login_required(login_url='/accounts/login/')
def EventManagerHome(request):
    events = Event.objects.all()
    order_completed = Order.objects.all()
    context = {'events': events, 'order_completed': order_completed}
    return render(request, 'eventmanager_home.html',context)

# Creo la vista per la creazione di un evento
@login_required(login_url='/accounts/login/')
def EventManagerCreateEvent(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                name = form.cleaned_data['name']
                slug = slugify(name)
                location = form.cleaned_data['location']
                description = form.cleaned_data['description']
                image = form.cleaned_data['image']
                ticket_Intero_cost = form.cleaned_data['ticket_Intero_cost']
                ticket_Ridotto_cost = form.cleaned_data['ticket_Ridotto_cost']
                ticket_Gruppo_cost = form.cleaned_data['ticket_Gruppo_cost']
                ticket_available = form.cleaned_data['ticket_available']
                published = form.cleaned_data['published']
                tags = request.POST.getlist('tags')
                event = Event(name=name, slug=slug, location=location,description=description, image=image,published = published, ticket_Intero_cost= ticket_Intero_cost, ticket_Ridotto_cost= ticket_Ridotto_cost, ticket_Gruppo_cost= ticket_Gruppo_cost)
                event.save() 
                for tag in tags:
                    event.tags.add(tag)
                from_date = form.cleaned_data['from_date']
                to_date = form.cleaned_data['to_date']
                date_list = [from_date + timedelta(days=x) for x in range((to_date - from_date).days + 1)]
                for date_item in date_list:
                    new_date = EventDates(date=date_item, event=event, tickets_available=ticket_available)
                    new_date.save()
            except Exception as e:
                print(e)
                return render(request, 'eventmanager_create_event.html', {'form': form, 'success': False})
            return HttpResponseRedirect('/event_manager/')
        else:
            return render(request, 'eventmanager_create_event.html', {'form': form, 'success': False})
    else:
        form = CreateEventForm()
        tags = EventTags.objects.all()
        return render(request, 'eventmanager_create_event.html', {'form': form, 'tags': tags})


# Creo la vista per l'aggiunta di date ad un evento'
def EventManagerAddDatesToEvent(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = AddDatesToEventForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            tickets_available=form.cleaned_data['tickets_available']
            date_list = [from_date + timedelta(days=x) for x in range((to_date - from_date).days + 1)]
            for date_item in date_list:
                new_date = EventDates(date=date_item, event=event , tickets_available=tickets_available)
                new_date.save()
            return HttpResponseRedirect('/event_manager/')
        else:
            return render(request, 'eventmanager_add_dates_to_event.html', {'form': form, 'success': False})
    else:
        form = AddDatesToEventForm()
        return render(request, 'eventmanager_add_dates_to_event.html', {'form': form})


# Creo la vista per la modifica di un evento
def EventManagerModifyEvent(request, event_id):
    
    if request.method == 'GET':
        event = get_object_or_404(Event, pk=event_id)
        tags = EventTags.objects.all()
        form_init = {'name': event.name,'slug': event.slug, 'location': event.location, 'description': event.description, 'image': event.image,
                                        'ticket_Intero_cost': event.ticket_Intero_cost,
                                        'ticket_Ridotto_cost': event.ticket_Ridotto_cost, 'ticket_Gruppo_cost': event.ticket_Gruppo_cost,
                                        'tags':tags}
        context = {'form_init': form_init,
                   'tags': tags}
        return render(request, 'eventmanager_modify_event.html',context)
    
    if request.method == 'POST':   
         event = Event.objects.get(pk=event_id) 
         form = ModifyEventForm(request.POST, request.FILES)
         if form.is_valid():
                event.name = form.cleaned_data['name']
                event.slug = slugify(event.name)
                event.location = form.cleaned_data['location']
                event.description = form.cleaned_data['description']
                event.image = form.cleaned_data['image']    
                event.ticket_Intero_cost = form.cleaned_data['ticket_Intero_cost']
                event.ticket_Ridotto_cost = form.cleaned_data['ticket_Ridotto_cost']
                event.ticket_Gruppo_cost = form.cleaned_data['ticket_Gruppo_cost']
                tags = request.POST.getlist('tags')           
                event.save()
                for tag in tags:
                    event.tags.add(tag)
                return HttpResponseRedirect('/event_manager/')
         else:
             return render(request, 'eventmanager_modify_event.html', {'form': form, 'success': False})
    else:
         return HttpResponseRedirect('/event_manager/')


# Creo la vista per la cancellazione di un evento
def EventManagerDeleteEvent(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return HttpResponseRedirect('/event_manager/')


# Creo la vista per la cancellazione di un ordine
@login_required(login_url='/accounts/login/')
def EventManagerDeleteOrder(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return HttpResponseRedirect('/event_manager/')


# Creo la vista per la modifica di un ordine
def EventManagerModifyOrder(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'GET':
        form = ModifyOrderForm(initial={'event': order.event, 'date': order.date, 'user': order.user, 'num_tickets_interi': order.num_tickets_interi,
                                        'num_tickets_ridotti': order.num_tickets_ridotti, 'num_tickets_gruppi': order.num_tickets_gruppi, 'total': order.total})
        context = {'form': form}
        return render(request, 'eventmanager_modify_order.html',context)
    
    if request.method == 'POST':
        form = ModifyOrderForm(request.POST)
        if form.is_valid():
            order.event = form.cleaned_data['event']
            order.date = form.cleaned_data['date']
            order.user = form.cleaned_data['user']
            order.num_tickets_interi = form.cleaned_data['num_tickets_interi']
            order.num_tickets_ridotti = form.cleaned_data['num_tickets_ridotti']
            order.num_tickets_gratuiti = form.cleaned_data['num_tickets_gratuiti']
            order.total = form.cleaned_data['total']
            order.save()
            return HttpResponseRedirect('/event_manager/')
        else:
            return render(request, 'eventmanager_modify_order.html', {'form': form, 'success': False})
    else:
        return HttpResponseRedirect('/event_manager/')
