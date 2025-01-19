

<form class="row g-3" method="POST" novalidate>
    {% csrf_token %}
    <div class="col-md-6 input-group">
        <span class="input-group-text" id="nome">Nome:</span>
        <input type="text" class="form-control" id="name" name="name" required>
    </div>
    <div class="col-md-6 input-group">
        <span class="input-group-text" id="location">location:</span>
        <input type="text" class="form-control" id="location" name="location" required>
    </div>
    <div class="col-md-2">
        <label for="from_date" class="form-label">Data Inizio</label>
        <input type="date" class="form-control" id="datepicker_from" name="from_date" required>
    </div>
    <div class="col-md-2">
        <label for="to_date" class="form-label">Data Fine</label>
        <input type="date" class="form-control" id="datepicker_to" name="to_date" required>
    </div>
    <div class="col-12">
        <label for="description" class="form-label">Descrizione dell'evento</label>
        <textarea class="form-control" id="description" name="description" rows="5" required></textarea>
    </div>
    <div class="col-md-4">
        <label for="ticket_Intero_cost" class="form-label">Costo Biglietto Intero</label>
        <input type="number" class="form-control" id="ticket_Intero_cost" name="ticket_Intero_cost" required>
    </div>
    <div class="col-md-4">
        <label for="ticket_Ridotto_cost" class="form-label"> Costo Biglietto Ridotto </label>
        <input type="number" class="form-control" id="ticket_Ridotto_cost" name="ticket_Ridotto_cost" required>
    </div>
    <div class="col-md-4">
        <div class="form-check">
            <label for="ticket_Gruppo_cost" class="form-label">Costo Biglietto Gratuito</label>
            <input type="number" class="form-control" id="ticket_Gruppo_cost" name="ticket_Gruppo_cost" required>
        </div>
    </div>
    <div class="col-3">
        <label for=image class="form-label">Immagine copertina evento</label>
        <input type="file" class="form-control" id="image" name="image" required>
    </div>
    <div class="col-3">
        <label for="ticket_available" class="form-label">Biglietti disponibili in ogni data</label>
        <input type="number" class="form-control" id="ticket_available" name="ticket_available" required>
    </div>
    <div class="col-12">
        <button id="submit" type="submit" class="btn btn-primary">Crea evento</button>
    </div>
</form>