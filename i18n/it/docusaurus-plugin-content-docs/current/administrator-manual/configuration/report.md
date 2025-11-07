---
title: Report
sidebar_position: 12
---

Il nuovo report unificato di NethVoice consente di utilizzare un'unica interfaccia web per consultare:

- report code
- report chiamate e costi (CDR, Call Detail Record)

Il report è accessibile all'indirizzo `https://<server_name>/pbx-report`. Ogni utente può accedere con le stesse credenziali utilizzate all'interno del NethVoice CTI. Le tabelle e i grafici visualizzati saranno filtrati in base al profilo NethVoice CTI associato all'utente. Accedendo con l'utente admin di NethVoice, sarà possibile visualizzare sempre tutti i dati.

Il report consente l'accesso solo ai dati storicizzati a partire dal giorno precedente, indietro fino alla data di primo utilizzo del centralino. Tutte le notti un processo elabora gli eventi della giornata e li rende disponibili per visualizzare grafici e tabelle. Quindi, al termine della prima installazione, è necessario attendere il giorno successivo per consultare il report.

Il report è disponibile con l'installazione dell'istanza di NethVoice.

Per il dettaglio dei Report fare riferimento al [Manuale Utente - Report](../../user-manual/nethcti/report.md).

All'amministratore è riservata anche la parte delle impostazioni.

## Impostazioni {#impostazioni}

Le impostazioni dei report sono accessibili cliccando il pulsante con l'icona di ingranaggio nella barra degli strumenti in alto a destra. Il pulsante è visibile soltanto se è stato effettuato il login con l'utenza `admin`.

Le impostazioni sono organizzate nelle seguenti sezioni:

- Generali
- Destinazioni
- Costi
- Ripristina impostazioni

### Generali {#generali}

In questa sezione è possibile configurare le seguenti impostazioni:

- **Inizio/fine orario lavorativo**: questa informazione è usata dai grafici che tracciano dati in riferimento alle fasce orarie della giornata
- **Numero massimo di risultati**: indica quanti risultati possono essere mostrati da un grafico tabellare. Se questo limite viene raggiunto, appare un'icona di avvertimento di fianco al titolo del grafico
- **Durata chiamate nulle**: le chiamate con durata minore o uguale a questo valore sono considerate nulle
- **Valuta**: usata per visualizzare il costo delle chiamate

### Destinazioni {#destinazioni}

Le destinazioni sono utilizzate per calcolare i costi delle chiamate. La configurazione predefinita prevede le seguenti destinazioni:

- `National`: numerazioni nazionali
- `Mobile`: numerazioni cellulari
- `International`: numerazioni estere
- `Emergency`: numerazioni di emergenza
- `PayNumber`: numerazioni a tariffa maggiorata

È possibile aggiungere nuove destinazioni così come rimuovere quelle esistenti.

Espandendo la voce **Configura i prefissi di destinazione** è possibile configurare la destinazione di una chiamata tramite il prefisso del numero di telefono composto. Siccome ogni prefisso definito può avere lunghezza variabile e sono quindi possibili sovrapposizioni, la destinazione di una numerazione telefonica è stabilita selezionando il prefisso più specifico (ovvero il più *lungo*). Ad esempio, supponendo di associare il prefisso `0039` alla destinazione `National`, e il prefisso `00393` alla destinazione `Mobile`, una chiamata in uscita con numerazione `00393401234567` avrà come destinazione `Mobile`, poiché il prefisso `00393` è più specifico rispetto al prefisso `0039`.

### Costi {#costi}

Dopo aver configurato le destinazioni delle chiamate e i prefissi di destinazione, è possibile configurare i costi delle chiamate. Il costo di una telefonata è determinato dal fascio PBX e dalla destinazione della chiamata. Per configurare un nuovo costo, quindi, è sufficiente specificare il fascio, la destinazione e la relativa tariffa al minuto.

#### Esempio di configurazione di un nuovo costo {#esempio-nuovo-costo}

Si supponga di avere attivato su un fascio PBX di nome `trunk_1` un contratto telefonico secondo il quale le chiamate verso la Spagna hanno una tariffazione di 0.01 EUR al minuto. Per far sì che il costo di queste chiamate sia calcolato e mostrato nel report, è necessario seguire i seguenti passi:

- Accedere al report con utenza `admin`
- Accedere alle impostazioni
- Definire una nuova destinazione, denominandola ad esempio `Spagna`
- Configurare un nuovo prefisso di destinazione, indicando il prefisso nazionale spagnolo (`0034` oppure `+34`, in funzione di come è stato configurato il centralino) e selezionando `Spagna` come destinazione
- Configurare un nuovo costo, selezionando il fascio `trunk_1`, la destinazione `Spagna` e indicando `0.01 EUR` come costo al minuto

Da questo momento, ogni notte un processo elaborerà i costi delle chiamate effettuate dal fascio `trunk_1` verso la Spagna. I costi delle chiamate sono quindi disponibili dal giorno successivo alla configurazione.

### Ripristina impostazioni {#ripristina-impostazioni}

**Avvertimento**

Il ripristino delle impostazioni è irreversibile

In questa sezione è presente un pulsante per ripristinare tutte le impostazioni ai loro valori predefiniti. Cliccando il pulsante e confermando la scelta saranno ripristinate tutte le impostazioni contenute nella sezione **Generali**, tutte le destinazioni, i prefissi di destinazione e saranno eliminate tutte le configurazioni dei costi.
