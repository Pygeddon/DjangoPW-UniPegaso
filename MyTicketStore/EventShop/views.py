from django.shortcuts import render,HttpResponseRedirect
from EventManager.models import Event, EventDates, Order
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Creo le viste necessarie per la gestione dell'applicazione EventShop


#Questa vista riceve i dettagli di acquisto di un evento in una determinata data. Se confermata
#reindirizza alla vista EventShopBuyTicketStep2
def EventShopBuyTicket(request):    
    if (request.method == 'GET'):
        if ('event_id' in request.GET and 'date' in request.GET):
            event_id = request.GET.get('event_id')
            event = Event.objects.get(id=event_id)
            date = request.GET.get('date')
            context = {
                'event': event,
                'date': date
            }
            return render(request, 'eventshop_buyticket_step1.html', context)
        else:
            return render(request, 'eventshop_buyticket_error.html')
    else:
        return render(request, 'eventshop_buyticket_error.html')


#Questa vista mostra il resoconto dell'acquisto che si sta effettuanfdo e permette di procedere al pagamento
def EventShopBuyTicketStep2(request):
    if (request.method == 'POST'):
        if request.POST['event_id'] and request.POST['date']:
            event_id = request.POST['event_id']
            event = Event.objects.get(id=event_id)
            date = request.POST['date']
            converted_date = datetime.strptime(date, '%d-%m-%Y').date()
            date_of_event = EventDates.objects.get(event=event, date=converted_date)
            print(converted_date)
            intero_cost = event.ticket_Intero_cost
            ridotto_cost = event.ticket_Ridotto_cost
            tickets_interi = int(request.POST['num_tickets_interi'])
            tickets_ridotti = int(request.POST['num_tickets_ridotti'])
            tickets_gruppi = int(request.POST['num_tickets_gruppi'])    
            total = (tickets_interi * intero_cost) + (tickets_ridotti * ridotto_cost) + (tickets_gruppi * event.ticket_Gruppo_cost)
            print(total)
            tickets = {'interi' : tickets_interi,'ridotti' : tickets_ridotti,
                        'gruppi' : tickets_gruppi, 'totale' : float(total) }
            date = request.POST['date']
            request.session['event_id'] = event_id
            request.session['date_id'] = date_of_event.id
            request.session['tickets'] = tickets
            context = {
                'event': event,
                'date': date,
                'tickets': tickets
               
            }
            return render(request, 'payment.html', context)
    else:
        return  render(request, 'eventshop_buyticket_error.html')

#Questa vista permette di creare un ordine per l'evento selezionato. L'acquisto vero e proprio avviene
@login_required(login_url='/accounts/login/')
def EventShopCreateOrder(request):
    if (request.session['event_id'] and request.session['date_id'] and request.session['tickets']):
        user = request.user
        event_id = request.session['event_id']
        date_id = request.session['date_id']
        tickets = request.session['tickets']
        event = Event.objects.get(id=event_id)
        date = EventDates.objects.get(event=event, id=date_id)
        """
        Update the tickets available for the event date
        """
        date.tickets_available -= int(tickets['interi']) + int(tickets['ridotti']) + int(tickets['gruppi'])
        date.save()
        order = Order(event=event, date=date,
                       user = user,
                       num_tickets_interi=tickets['interi'], 
                       num_tickets_ridotti=tickets['ridotti'], 
                       num_tickets_gruppi=tickets['gruppi'],
                       total=tickets['totale']) 
        order.save()
        return HttpResponseRedirect('/event_store')