from django import forms

class CreateEventForm(forms.Form):
    name = forms.CharField(label='Event Name', max_length=100)  
    location = forms.CharField(label='Location', max_length=100)
    from_date = forms.DateField(label='From Date')
    to_date = forms.DateField(label='To Date')
    description = forms.CharField(label='Description', widget=forms.Textarea)
    image = forms.ImageField(label='Image')
    ticket_Intero_cost = forms.DecimalField(label='Ticket Intero Cost')
    ticket_Ridotto_cost = forms.DecimalField(label='Ticket Ridotto Cost')
    ticket_Gruppo_cost = forms.DecimalField(label='Ticket Gruppo Cost')
    ticket_available = forms.IntegerField(label='Tickets Available')
    published = forms.ChoiceField(label='Published', choices=[('draft', 'Draft'), ('published', 'Published')])

    widgets = {
        'from_date': forms.DateInput(attrs={'type': 'date','id': 'from_date'}),
        'to_date': forms.DateInput(attrs={'type': 'date', 'id': 'to_date'}),
        'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        'image': forms.FileInput(),
        'name': forms.TextInput(attrs={'placeholder': 'Event Name'}),
        'location': forms.TextInput(attrs={'placeholder': 'Location'}),
        'image' : forms.FileInput(attrs={'accept': 'image/*'}),
        'ticket_Intero_cost': forms.NumberInput(attrs={'placeholder': 'Ticket Intero Cost'}),
        'ticket_Ridotto_cost': forms.NumberInput(attrs={'placeholder': 'Ticket Ridotto Cost'}),
        'ticket_Gruppo_cost': forms.NumberInput(attrs={'placeholder': 'Ticket Gruppo Cost'}),
        'ticket_available': forms.NumberInput(attrs={'placeholder': 'Tickets Available for Date'}),
        'published': forms.Select(attrs={'placeholder': 'Published'}),
    }

class ModifyEventForm(forms.Form):
    name = forms.CharField(label='Event Name', max_length=100)  
    location = forms.CharField(label='Location', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    image = forms.ImageField(label='Image')
    ticket_Intero_cost = forms.DecimalField(label='Ticket Intero Cost')
    ticket_Ridotto_cost = forms.DecimalField(label='Ticket Ridotto Cost')
    ticket_Gruppo_cost = forms.DecimalField(label='Ticket Gruppo Cost')

    widgets = {
        'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        'image': forms.FileInput(),
        'name': forms.TextInput(attrs={'placeholder': 'Event Name'}),
        'location': forms.TextInput(attrs={'placeholder': 'Location'}),
        'image' : forms.FileInput(attrs={'accept': 'image/*'}),
        'ticket_Intero_cost': forms.NumberInput(attrs={'placeholder': 'Ticket Intero Cost'}),
        'ticket_Ridotto_cost': forms.NumberInput(attrs={'placeholder': 'Ticket Ridotto Cost'}),
        'ticket_Gruppo_cost': forms.NumberInput(attrs={'placeholder': 'Ticket Gruppo Cost'}),
    }

class ModifyOrderForm(forms.Form):
     event = forms.CharField(label='Event Name', max_length=100)
     dete = forms.DateField(label='Date')
     user = forms.CharField(label='User')
     num_tickets_interi = forms.IntegerField(label='Number of Intero Tickets')
     num_tickets_ridotti = forms.IntegerField(label='Number of Ridotti Tickets')
     num_tickets_gruppi= forms.IntegerField(label='Number of Group Tickets')
     total = forms.DecimalField(label='Total')
     widgets = {
         'event': forms.TextInput(attrs={'placeholder': 'Event Name'}),
         'date': forms.DateInput(attrs={'type': 'date'}),
         'user': forms.TextInput(attrs={'placeholder': 'User'}),
         'num_tickets_interi': forms.NumberInput(attrs={'placeholder': 'Number of Intero Tickets'}),
         'num_tickets_ridotti': forms.NumberInput(attrs={'placeholder': 'Number of Ridotti Tickets'}),
         'num_tickets_gruppi': forms.NumberInput(attrs={'placeholder': 'Number of Group Tickets'}),
         'total': forms.NumberInput(attrs={'placeholder': 'Total'}),
     }


class AddDatesToEventForm(forms.Form):
    from_date = forms.DateField(label='Date')
    to_date = forms.DateField(label='Date')
    tickets_available = forms.IntegerField(label='Tickets Available')
    widgets = {
        'from_date': forms.DateInput(attrs={'type': 'date', id: 'id_from_date'}),
        'to_date': forms.DateInput(attrs={'type': 'date', id: 'id_to_date'}),
        'tickets_available': forms.NumberInput(attrs={'placeholder': 'Tickets Available for Date'}),
    }