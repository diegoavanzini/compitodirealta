## Gestione compiti

Applicazione Python da terminale per inserire e consultare compiti con una data di alert automatica.
Il progetto ha scopo didattico: e pensato per esercitarsi con Python, gestione date, persistenza su file e test unitari.
Il progetto salva i dati su file di testo e include test unitari per le funzioni principali.

## Obiettivo

Consentire una gestione semplice dei compiti con:
- inserimento di titolo e descrizione;
- data di esecuzione;
- calcolo della data di avviso (1 giorno prima);
- persistenza locale su file.

## Funzionalita implementate

- Inserimento di un nuovo compito da CLI.
- Lettura e visualizzazione dei compiti salvati.
- Calcolo automatico della data di alert.
- Validazione della data (non puo essere nel passato).
- Salvataggio strutturato su file `compiti.txt`.
- Test unitari con `pytest`.

## Struttura del progetto

- `main.py`: punto di ingresso dell'applicazione da terminale.
- `src/alert_date.py`: logica per il calcolo della data di alert.
- `src/data_file.py`: funzioni di lettura/scrittura file.
- `tests/test_alert_date_calculator.py`: test sul calcolo della data.
- `tests/test_data_file.py`: test su persistenza file.
- `compiti.txt`: archivio dei compiti.

## Formato dei dati

Ogni riga in `compiti.txt` rappresenta un compito nel formato:

`data_alert;titolo;descrizione`

Esempio:

`11/04/2026;Consegna progetto;Preparare presentazione finale`

## Come eseguire il progetto

1. Attiva l'ambiente virtuale (se presente).
2. Avvia l'applicazione:

```bash
python main.py
```

3. Scegli:
- `1` per aggiungere un compito;
- `2` per visualizzare i compiti esistenti.

## Eseguire i test

```bash
pytest -q
```

## Stato sviluppo

- [x] inserimento di un compito
- [x] calcolo della data di alert
- [x] unit test
- [x] persistenza
- [x] persistenza strutturata
- [x] README completo
- [x] crea Makefile
- [ ] aggiungere modifica evento
- [ ] aggiungere cancellazione evento
- [ ] aggiungere sito web con form di inserimento
- [ ] aggiungere configurazione sistemi di notifica
- [ ] aggiungere configurazione notifiche ricorrenti
- [ ] aggiungere integrazione email
- [ ] aggiungere integrazione alexa
- [ ] aggiungere configurazione notifica a piu utenti
