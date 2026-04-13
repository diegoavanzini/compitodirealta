## Gestione compiti

Applicazione Python da terminale per creare eventi su Google Calendar.
Il progetto nasce come esercizio didattico su Python, gestione date, persistenza locale e integrazione API esterne.

## Stato attuale

Il flusso principale e ora basato su Google Calendar:

- inizializzazione client Calendar con OAuth2;
- creazione di un evento da CLI;
- salvataggio e riuso del token locale;
- test unitari ancora presenti per i moduli storici di logica data/file.

## Prerequisiti

- Python 3.10+
- ambiente virtuale attivo (consigliato)
- credenziali OAuth Google Calendar in `credentials.json`
- file `token.json` generato al primo login

Dipendenze principali usate nel codice:

- `google-auth`
- `google-auth-oauthlib`
- `google-api-python-client`
- `pytest` (per i test)

## Configurazione Google Calendar

1. Crea un progetto Google Cloud e abilita Google Calendar API.
2. Crea credenziali OAuth Client (Desktop app).
3. Scarica il file credenziali e salvalo come `credentials.json` nella root del progetto.
4. Al primo avvio si aprira il browser per autorizzare l'accesso.
5. Al termine verra creato `token.json` per i successivi avvii.

Nota: se cambi gli scope OAuth, elimina `token.json` e ripeti il login.

## Come eseguire

Con Makefile:

```bash
make run
```

Oppure direttamente:

```bash
python main.py
```

Durante l'esecuzione:

- `1`: richiede titolo, descrizione e data (`dd/mm/yyyy hh:mm`) e crea un evento su calendario `primary`
- `q`: esce dal programma

## Test

```bash
make test
```

oppure:

```bash
pytest -q
```

## Struttura progetto

- `main.py`: entrypoint CLI e invocazione classe Calendar
- `src/gcalendar.py`: classe `google_calendar` con autenticazione e creazione eventi
- `src/alert_date.py`: logica storica per calcolo data alert
- `src/data_file.py`: logica storica di persistenza su file
- `tests/test_alert_date_calculator.py`: test modulo date
- `tests/test_data_file.py`: test modulo file
- `compiti.txt`: archivio locale storico
- `credentials.json`: credenziali OAuth (locale)
- `token.json`: token OAuth generato al primo accesso

## Stato sviluppo

- [x] inserimento compito/evento da CLI
- [x] integrazione Google Calendar
- [x] creazione evento su calendario primary
- [x] test unitari moduli storici
- [x] Makefile (`run`, `test`, `clean`)
- [ ] modifica evento Google Calendar
- [ ] cancellazione evento Google Calendar
- [ ] interfaccia web per inserimento
- [ ] configurazione sistemi di notifica
- [ ] notifiche ricorrenti avanzate
- [ ] integrazione email
- [ ] integrazione Alexa
- [ ] notifica multi-utente
