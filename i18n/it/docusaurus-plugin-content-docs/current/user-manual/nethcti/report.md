---
title: Report
sidebar_position: 4
---

Il nuovo report unificato di NethVoice consente di utilizzare un'unica interfaccia web per consultare:

- report code
- report chiamate e costi (CDR, Call Detail Record)

Il report è accessibile all'indirizzo `https://<server_name>/pbx-report`. Ogni utente può accedere con le stesse credenziali utilizzate all'interno del NethVoice CTI. Le tabelle e i grafici visualizzati saranno filtrati in base al profilo NethVoice CTI che l'amministratore ha associato all'utente.

Il report consente l'accesso solo ai dati storicizzati a partire dal giorno precedente, indietro fino alla data di primo utilizzo del centralino.

## Report code {#report-code}

Il report code mostra molteplici informazioni associate alle code del centralino, come ad esempio dati sugli agenti e sulle loro sessioni di lavoro, sulle performance delle code, sulle aree geografiche di provenienza delle chiamate e sulle durate dei tempi di attesa.

Le varie sezioni sono dotate di documentazione inline per spiegare le varie funzionalità.

Il modulo si divide in due sezioni principali, quelle Dati e Distribuzione dove vengono racconti i dati statistici, e quella dei Grafici dove questi dati vengono utilizzati per produrre dei grafici che semplificano la loro analisi.

Accedendo al modulo si entra nella Dashboard che riepiloga i grafici più significativi.

### Dati {#dati}

#### Riepilogo {#riepilogo}

In questa sezione si trovano le chiamate ricevute per ogni Coda configurata in NethVoice suddivise in:

- **Chiamate evase**
  - Totale
  - Attesa massima minima e media
  - Durata massima minima e media
  - Posizione massima e media di entrata in coda
- **Chiamate fallite**
  - Totale
  - Attesa massima minima e media
  - Posizione massima media di entrata e di uscita

È possibile utilizzare il filtro per creare una ricerca più particolareggiata nel tempo o per singola Coda ed esportare il risultato in un file `.xls`

#### Per agente {#per-agente}

In questa sezione si trovano le attività degli agenti delle varie code mostrando:

- Tempo di lavoro
- Tempo di pausa ed effettivo
- Chiamate risposte
- Chiamate non risposte
- Totale di conversazione
- Chiamate all'ora
- Percentuale di occupazione
- Durata massima, minima e media delle chiamate

È possibile utilizzare il filtro per creare una ricerca più particolareggiata nel tempo o per singolo Agente e/o Coda ed esportare il risultato in un file `.xls`

#### Per sessione {#per-sessione}

In questa sezione si trovano le sessioni lavorative e di pausa degli agenti delle code, vengono mostrati:

- Coda
- Agente
- Tipo di sessione
- Inizio e fine della sessione
- Durata
- Motivazione della pausa se si tratta di una sessione di questo tipo

È possibile utilizzare il filtro per creare una ricerca più particolareggiata nel tempo o per singolo Agente e/o Coda ed esportare il risultato in un file `.xls`

#### Per chiamante {#per-chiamante}

In questa sezione si trovano i dati relativi alle chiamate entrate nelle code raggruppate per numero chiamante.

È possibile utilizzare il filtro per creare una ricerca più particolareggiata nel tempo o per singola Coda o numero chiamante ed esportare il risultato in un file `.xls`

#### Per chiamata {#per-chiamata}

In questa sezione si trovano i dati relativi alle chiamate entrate nelle code, lo scopo principale è mostrarne l'esito. Vengono visualizzati:

- Data
- Chiamante
- Coda chiamata
- Agente (se si tratta di una chiamata gestita)
- Posizione in coda
- Tempo di attesa
- Durata
- Esito

È possibile utilizzare il filtro per creare una ricerca più particolareggiata nel tempo o per singola Coda o numero chiamante ed esportare il risultato in un file `.xls`

#### Per chiamate non gestite {#per-chiamate-non-gestite}

In questa sezione si trovano i dati relativi alle chiamate che non sono state gestite dagli operatori.

È possibile utilizzare il filtro per creare una ricerca più particolareggiata nel tempo o per singola Coda o numero chiamante ed esportare il risultato in un file `.xls`

#### IVR {#ivr}

In questa sezione si trovano le chiamate che hanno avuto come destinazione un IVR configurato in NethVoice, viene visualizzata:

- Nome dell'IVR
- Scelta effettuata dal chiamante
- Totale delle chiamate

È possibile utilizzare il filtro per creare una ricerca più particolareggiata nel tempo o per singola Rotta in Entrata ed esportare il risultato in un file `.xls`

#### Performance {#performance}

In questa sezione vengono riassunte le performance delle varie code mostrando:

- i totali e le percentuali delle chiamate:
  - Evase
  - Non evase
  - Nulle
- i dati totali di attesa e durata

Viene anche mostrata la qualità del servizio offerta delle code raggruppando le chiamate per tempo di attesa.

È possibile utilizzare il filtro per creare una ricerca più particolareggiata nel tempo o per singola Coda ed esportare il risultato in un file `.xls`

### Distribuzione {#distribuzione}

#### Oraria {#oraria}

In questa sezione le chiamate entranti nelle code vengono distribuite nell'arco temporale giornaliero e suddivise anche per chiamate evase ed inevase.

È possibile utilizzare il filtro per creare una ricerca più particolareggiata nel tempo o per singola Coda ed esportare il risultato in un file `.xls`

#### Geografica {#geografica}

In questa sezione le chiamate entranti nelle Code vengono raggruppate per zona geografica e possono essere divise per Regione, Provincia o Prefisso.

È possibile utilizzare il filtro per creare una ricerca più particolareggiata nel tempo o per singola Coda ed esportare il risultato in un file `.xls`

### Grafici {#grafici}

#### Carico {#carico}

In questa sezione vengono mostrati i grafici per la distribuzione del totale delle chiamate entranti suddivise nelle varie Code nella sezione di tempo scelta e di seguito divise per la zona geografica di provenienza scelta.

#### Oraria {#grafici-oraria}

In questa sezione vengono mostrati i grafici per la distribuzione oraria del totale delle chiamate entranti suddivise nelle varie Code nella sezione di tempo scelta.

#### Per Agente {#grafici-per-agente}

In questa sezione vengono mostrati i grafici per il totale delle chiamate evase dagli agenti delle Code nella sezione di tempo scelta.

#### Per zona {#per-zona}

In questa sezione vengono mostrati i grafici per il totale delle chiamate entranti suddivise nelle varie Code nella sezione di tempo scelta in base alla zona geografica di provenienza.

#### Posizione Coda {#posizione-coda}

In questa sezione vengono mostrati i grafici per la posizione di entrata delle chiamate in Coda suddivisi per le varie Code.

#### Durata media {#durata-media}

In questa sezione vengono mostrati i grafici per la durata media delle chiamate entranti suddivise nelle varie Code nella sezione di tempo scelta in base all'orario di entrata.

#### Attesa Media {#attesa-media}

In questa sezione vengono mostrati i grafici per l'attesa media delle chiamate entranti suddivise nelle varie Code nella sezione di tempo scelta in base all'orario di entrata.

#### Richiamata {#richiamata}

In questa sezione vengono mostrati i grafici per le chiamate effettuate dagli agenti con successo alle numerazioni che hanno avuto un fallimento in coda.

## Report chiamate & costi (CDR) {#cdr-report}

Il report CDR mostra informazioni aggregate e di dettaglio relative al registro chiamate. Oltre alla sezione **Dashboard**, che presenta alcuni grafici riepilogativi, sono presenti le seguenti sezioni:

- **Dati centralino**: informazioni sulle chiamate in ingresso, in uscita e interne al centralino
- **Dati personali**: informazioni sulle chiamate interne, ricevute, o effettuate dall'utente loggato

I grafici delle sezioni **Dati centralino** e **Dati personali** presentano la stessa struttura, mostrando:

- Un grafico riepilogativo espandibile che mostra dati sui totali e le durate delle chiamate
- Un registro chiamate tabellare che mostra numero sorgente, numero di destinazione, esito chiamata, durata e costo. Cliccando il pulsante **Mostra dettagli** è possibile visualizzare ulteriori dettagli di ciascuna chiamata

La prima volta che si accede al report CDR, viene mostrata una finestra di dialogo che suggerisce di configurare i costi delle chiamate al fine di includerli nel report. Per ulteriori informazioni riguardo i costi delle chiamate si veda la sezione [Manuale Amministratore - Impostazioni Report](../../administrator-manual/configuration/report.md#costi).

Le varie sezioni sono dotate di documentazione inline per spiegare le varie funzionalità.

## Interfaccia utente {#interfaccia-utente}

L'interfaccia utente è comune a *report code* e *report CDR*, ed è organizzata in tre aree principali:

- Menu laterale
- Filtri
- Grafici

:::note
Gli utenti con account `admin` possono accedere a opzioni di configurazione aggiuntive. Per ulteriori informazioni, consulta [Manuale Amministratore - Impostazioni Report](../../administrator-manual/configuration/report.md).
:::

### Menu laterale {#menu-laterale}

Il menu laterale consente la navigazione dei report e contiene:

- Un selettore per passare dalla consultazione del report code a quella del report CDR e viceversa
- Una casella di ricerca per trovare rapidamente una vista o un grafico di interesse
- La struttura completa del report corrente (code o CDR), organizzato in sezioni e viste. Ogni sezione può aggregare un insieme di viste oppure essere autocontenuta (ad es. la sezione *Dashboard*)

### Filtri {#filtri}

L'area dei filtri consente di configurare l'intervallo temporale e i parametri per generare il report della vista corrente. La generazione del report può essere avviata cliccando il pulsante **Cerca**. Il pulsante **Salva ricerca** consente di salvare una specifica configurazione dei filtri, in modo che possa essere riutilizzata rapidamente.

Nell'angolo in alto a destra dell'area filtri sono presenti i seguenti pulsanti, attraverso i quali è possibile (da sinistra a destra):

- Nascondere/mostrare il pannello dei filtri
- Selezionare lo schema di colori utilizzato dai grafici
- Accedere alle impostazioni dei report; questa funzionalità è disponibile soltanto se è stato effettuato l'accesso con l'utenza `admin`
- Eseguire il logout

### Grafici {#grafici-area}

L'area dei grafici costituisce quella di maggior interesse per l'utente e costituisce il corpo del report della vista corrente. Ciascun grafico può essere esportato in almeno uno dei seguenti formati: CSV, PNG e PDF. Per motivi di leggibilità, alcuni grafici mostrano soltanto i dati più rilevanti: attraverso il pulsante **Mostra dettagli** è possibile accedere al set completo dei dati del grafico. Alcuni tipologie di grafico consentono di nascondere uno o più set di dati che si vuole temporaneamente trascurare: per farlo è sufficiente cliccare sul relativo nome nella legenda del grafico.
