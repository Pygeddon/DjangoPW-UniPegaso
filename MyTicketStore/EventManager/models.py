from django.db import models
from django.contrib.auth.models import User
from django.db.models import ManyToManyField

# Creiamo i nostri modelli a partire dal diagramma ER realizzato in precedenza

class EventTags(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

        
class Event(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique_for_date='published')
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    ticket_Intero_cost = models.DecimalField(max_digits=6, decimal_places=2)
    ticket_Ridotto_cost = models.DecimalField(max_digits=6, decimal_places=2)
    ticket_Gruppo_cost  = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    tags = ManyToManyField(EventTags, related_name='events')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventi'



class EventDates(models.Model):
    date = models.DateField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='dates')
    tickets_available = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.date.strftime('%d-%m-%Y')
    
    class Meta:
        verbose_name = 'Data evento'
        verbose_name_plural = 'Date eventi'

class Order(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.ForeignKey(EventDates, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_tickets_interi = models.IntegerField()
    num_tickets_ridotti = models.IntegerField()
    num_tickets_gruppi = models.IntegerField()
    total = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.event.name + ' - ' + self.date.date.strftime('%d-%m-%Y')
    
    class Meta:
        verbose_name = 'Ordine'
        verbose_name_plural = 'Ordini'
