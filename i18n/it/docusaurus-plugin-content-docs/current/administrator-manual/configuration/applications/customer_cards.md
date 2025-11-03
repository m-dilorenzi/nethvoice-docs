---
title: Schede cliente
sidebar_position: 1
---

# Schede cliente

La sezione *schede cliente* abilita il raggruppamento di informazioni da database esterni al PBX e la loro visualizzazione durante le chiamate. Ad esempio, quando si riceve una chiamata da un cliente specifico, recuperare informazioni dal database relative alle loro fatture o eventuali pagamenti in sospeso e valutare se fornire assistenza o meno.

Per creare una nuova scheda cliente, segui questi passaggi:

#### Fonti della rubrica

Fai clic su `Crea nuova fonte` e completa il modulo che appare:

- `Tipo di database`: Specifica il tipo di database da cui verranno recuperate le informazioni.
- `Nome database`: Specifica il nome del database a cui connettersi.
- `Indirizzo database`: Specifica l'indirizzo per la connessione al database (localhost, socket o IP esterno).
- `Porta database`: Specifica una porta per il database diversa da quella predefinita proposta.
- `Utente database`: Specifica l'utente per la connessione al database.
- `Password database`: Specifica la password per la connessione al database.
- `Connessione`: Premi il pulsante "Verifica" per testare l'accuratezza delle informazioni di connessione immesse.

Premi `Salva` per aggiungere l'origine del database. La fonte appena creata sarà elencata tra le fonti disponibili.

#### Modello

I modelli servono come progetto per le tue schede cliente. Utilizzano il motore `ejs`, che vanta una sintassi simile a JavaScript. Ciò consente di scrivere codice HTML utilizzando direttive specifiche disponibili sul [sito web di EJS](https://github.com/tj/ejs).

Per iniziare il processo di creazione, fai clic sul pulsante `Crea nuovo modello`:

- `Nome`: Specifica il nome del modello.
- `Risultati`: Questo campo contiene l'output della tua query in formato JSON. Utilizza il campo di testo per testare e vedere come apparirà il tuo modello HTML con i tuoi dati.
- `Codice (ejs)`: Immetti il codice del tuo modello in questo campo di testo, aderendo alla sintassi ejs e utilizzando i valori menzionati sopra (che sono essenzialmente le colonne dei risultati della tua query).
- `Anteprima`: Combinando i risultati e il codice ejs, vedrai l'output HTML corrispondente, che servirà come tua scheda cliente.

Il PBX offre già alcuni modelli predefiniti con codice HTML pre-scritto che puoi duplicare e modificare alterando il colore.

#### Schede cliente

Dopo aver creato l'origine dati e il modello per la tua scheda, questa sezione richiede di unire i due pezzi di informazioni per garantire la corretta creazione della scheda. Fai clic sul pulsante `Crea nuova scheda` e compila il modulo:

- `Nome`: Nome della scheda cliente.
- `Fonte`: Specifica l'origine del database creata in precedenza.
- `Modello`: Scegli il modello che hai creato in precedenza.
- `Profilo`: Seleziona il tipo di profilo utente a cui verrà visualizzata la scheda cliente che stai creando.
- `Query`: Inserisci la query che restituirà le informazioni pertinenti.
- `Rendering`: Premendo questo pulsante, la query verrà eseguita sull'origine specificata e i dati verranno inseriti nel modello selezionato, producendo l'output desiderato.

Premi il pulsante `Salva` per salvare la tua scheda cliente.

:::warning
Una volta creata la query e la scheda e verificato che tutto funzioni, utilizza la variabile `$NUMBER` per sostituire i parametri numerici nella tua query.
:::

Esempio:

Se la tua query è la seguente:

```
select * from phonebook where homephone like '%150' or workphone like '%850' or cellphone like '%150' or fax like '%850'
```

Dovrebbe essere cambiato a:

```
select * from phonebook where homephone like '%$NUMBER' or workphone like '%$NUMBER' or cellphone like '%$NUMBER' or fax like '%$NUMBER'
```

La variabile `$NUMBER` rappresenta l'ID del chiamante del PBX, riferendosi alla raccolta dei dati da visualizzare sulla scheda cliente.
