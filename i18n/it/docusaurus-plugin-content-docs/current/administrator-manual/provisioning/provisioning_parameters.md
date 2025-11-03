---
title: Parametri di provisioning
sidebar_position: 6
---

# Guida ai Parametri di Provisioning

Le funzioni dei telefoni che possono essere configurate tramite provisioning sono raggruppate in vari pannelli all'interno dell'interfaccia di amministrazione di NethVoice. Questa guida descrive i parametri di provisioning configurabili organizzati per categoria funzionale.

## Panoramica

Non tutti i modelli di telefoni offrono le stesse funzioni, quindi alcuni parametri o interi pannelli potrebbero non essere visualizzati per tutti i dispositivi.

**Priorità dei Parametri:** In generale, lasciare un campo vuoto o selezionare l'opzione `-` (segno meno) indica che viene utilizzato il valore ereditato da un contesto con priorità inferiore. La priorità più alta è data alle impostazioni del telefono, seguita in ordine discendente dalle impostazioni del modello e dalle impostazioni predefinite.

Fare riferimento a [Priorità di Configurazione del Telefono](./phone_provisioning.md#phone-configuration-priority) per ulteriori informazioni sulla gerarchia di configurazione.

## Tasti Soft

I **tasti soft** sono tasti telefonici programmabili designati per le funzioni di chiamata del telefono.

Se il telefono fornisce più tasti di quelli visualizzati nell'interfaccia di amministrazione di NethVoice, è disponibile un pulsante **Visualizza altro** per aggiungere tasti aggiuntivi.

A seconda del **Tipo**, potrebbero essere necessari anche i campi **Valore** e **Etichetta** come indicato nella tabella seguente.

:::info
Nella colonna Etichetta, il termine "predefinito" significa che se il campo Etichetta viene lasciato vuoto, il telefono assegnerà un'etichetta predefinita al tasto soft.
:::

| Tipo | Descrizione | Valore | Etichetta |
|------|-------------|--------|-----------|
| Inoltro | Abilita/disabilita lo stato di inoltro (inoltro incondizionato). Se abilitato, tutte le chiamate in ingresso vengono inoltrate al numero specificato | Numero di telefono o interno | Sì (predefinito) |
| DND | Abilita/disabilita lo stato non disturbare. Se abilitato, tutte le chiamate in ingresso vengono rifiutate | No | No |
| Richiamare | Richiama l'ultimo numero composto | No | Sì (predefinito) |
| Rispondere | Rispondi a una chiamata in corso all'interno specificato | Numero di telefono | Sì |
| Numero veloce | Chiama il numero dato premendo il tasto | Numero di telefono | Sì |
| Prelievo gruppo | Rispondi a una chiamata in corso per il gruppo di prelievo configurato | No (Il gruppo è configurato.) | No |
| Cronologia | Visualizza la schermata della cronologia delle chiamate | No | Sì (predefinito) |
| Menu | Mostra il menu di configurazione del telefono | No | Sì (predefinito) |
| Stato | Visualizza informazioni sullo stato del telefono (es. versione firmware, stato della registrazione) | No | Sì (predefinito) |
| Prefisso | Aggiungi le cifre specificate al numero composto | Le cifre del prefisso | Sì (predefinito) |
| LDAP | Visualizza la rubrica LDAP configurata sul telefono | No | Sì (predefinito) |

## Tasti Linea

I **tasti linea** sono tasti telefonici programmabili che assomigliano ai tasti soft ma sono progettati più specificamente per la gestione delle chiamate e il monitoraggio dello stato degli interni.

Se il telefono fornisce più tasti di quelli visualizzati nell'interfaccia di amministrazione di NethVoice, è disponibile un pulsante **Visualizza altro** per aggiungere tasti aggiuntivi.

A seconda del **Tipo**, i campi **Valore** e **Etichetta** potrebbero aver bisogno di essere compilati come descritto nella tabella seguente.

:::info
Nella colonna Etichetta, il termine "predefinito" significa che se il campo Etichetta viene lasciato vuoto, il telefono assegnerà un'etichetta predefinita al tasto linea.
:::

| Tipo | Descrizione | Valore | Etichetta |
|------|-------------|--------|-----------|
| Conferenza | Le chiamate attive vengono unite in una conferenza dove ogni partecipante può ascoltare e parlare con gli altri simultaneamente | No | Sì (predefinito) |
| Inoltro | Abilita/disabilita lo stato di inoltro (inoltro incondizionato). Se abilitato, tutte le chiamate in ingresso vengono inoltrate al numero specificato | Numero di telefono o interno | Sì (predefinito) |
| Trasferimento chiamata | Trasferisce la chiamata corrente al numero selezionato o a un altro numero composto al momento | Numero di telefono o interno | Sì |
| Attesa | Mette la chiamata corrente in attesa | No | Sì (predefinito) |
| DND | Abilita/disabilita lo stato Non Disturbare (DND). Se abilitato, tutte le chiamate in ingresso vengono rifiutate | No | No |
| Richiamare | Richiama l'ultimo numero composto | No | Sì (predefinito) |
| Rispondere | Rispondi a una chiamata in ingresso all'interno specificato | Numero di telefono | Sì |
| DTMF | Esegue una sequenza di toni DTMF (Dual-Tone Multi-Frequency) durante una chiamata | Sequenza di simboli o numeri | Sì |
| Accedi/Esci agente dinamico | Accedi/Esci dalla coda di chiamata | No | Sì |
| Segreteria telefonica | Controlla la segreteria telefonica | No | Sì (predefinito) |
| Numero veloce | Chiama il numero dato premendo il tasto | Numero di telefono | Sì |
| Linea | Seleziona un'altra linea | No | Sì (predefinito) |
| BLF | Monitora lo stato dell'interno selezionato e, a seconda del suo stato, esegue un prelievo o un numero veloce quando premuto | Numero di telefono | Sì |
| URL | Esegue una richiesta HTTP GET all'indirizzo web specificato | Indirizzo web (URL) | Sì |
| Prelievo gruppo | Rispondi a una chiamata in corso per il gruppo di prelievo configurato | No (il gruppo è configurato) | No |
| Multicast paging | Invia audio direttamente all'interno configurato per il paging multicast | Numero di telefono | Sì (predefinito) |
| Registra | Avvia la registrazione audio della chiamata attiva | No | Sì (predefinito) |
| Prefisso | Aggiungi le cifre specificate al numero composto | Le cifre del prefisso | Sì (predefinito) |
| Blocco telefono | Attiva la funzione di blocco del telefono, limitando l'accesso ai tasti e all'interfaccia. La sequenza di sblocco deve essere configurata secondo la documentazione del telefono | No | Sì (predefinito) |
| LDAP | Mostra la rubrica LDAP configurata sul telefono | No | Sì (predefinito) |

## Tasti di Espansione

I **Tasti di Espansione** sono pulsanti programmabili su moduli di espansione, dispositivi che possono essere collegati al telefono per aumentare il numero di tasti disponibili.

Se il modulo di espansione fornisce più tasti di quelli visualizzati nell'interfaccia di amministrazione di NethVoice, è disponibile un pulsante **Visualizza altro** per aggiungere tasti aggiuntivi.

I tasti di espansione sono configurati in modo simile ai [Tasti Linea](#tasti-linea), quindi fare riferimento a quella sezione per i tipi e i parametri disponibili.

## Schermo e Suoneria

Questa sezione consente la configurazione delle impostazioni di visualizzazione e avviso audio del telefono:

- **Selezione Suoneria**: Ogni telefono ha alcune suonerie predefinite che possono essere selezionate in base al loro numero progressivo. Dove supportato, è possibile scegliere anche una suoneria personalizzata, che deve essere caricata nel campo descritto di seguito.

- **Gestione Suoneria Personalizzata**: Seleziona un file audio per la suoneria personalizzata precedentemente caricato, o caricane uno nuovo aprendo il modulo di gestione dedicato. Il formato audio deve essere compatibile con le specifiche del produttore del telefono.

- **Immagine di Sfondo**: Seleziona un file immagine per lo sfondo dello schermo del telefono, o carica una nuova tramite il pannello di gestione dedicato. Il formato immagine deve essere compatibile con le specifiche del produttore del telefono.

- **Immagine Screen Saver**: Seleziona un file immagine per lo screen saver, o carica una nuova tramite il pannello di gestione.

- **Attivazione Screen Saver**: Intervallo di tempo dopo il quale lo screen saver viene attivato.

- **Spegnimento Retroilluminazione**: Intervallo di tempo dopo il quale lo schermo abbassa la luminosità o spegne la retroilluminazione dello schermo.

- **Luminosità Schermo**: Seleziona il livello di luminosità dello schermo.

- **Contrasto Schermo**: Seleziona il livello di contrasto dello schermo.

## Preferenze

Questa sezione contiene importanti parametri di configurazione per il funzionamento del telefono:

### Impostazioni di Ora

- **Indirizzo Server NTP**: Il nome host o l'indirizzo IP del server Network Time Protocol (NTP) per impostare automaticamente l'ora del telefono.

- **Fuso Orario**: Imposta il fuso orario del telefono, necessario per gli aggiustamenti dell'ora legale.

- **Formato Ora**: Scelta del formato ora/data visualizzato sullo schermo del telefono.

- **Formato Data**: Scelta del formato data visualizzato sullo schermo del telefono.

### Programma Provisioning

- **Programma Provisioning**: 
  - *Solo all'avvio*: I telefoni rinnovano la loro configurazione dopo l'accensione o il riavvio
  - *Ogni giorno*: I telefoni rinnovano autonomamente la loro configurazione a un'ora casuale durante la notte

### Trasferimento Chiamata

- **Modalità Trasferimento per Tasti Linea**: Specifica come i tasti linea trasferiscono la chiamata in corso a un altro interno:
  - **Nuova Chiamata**: Avvia una nuova chiamata all'interno configurato sul tasto linea, mettendo la chiamata corrente in attesa
  - **Consultiva**: Mette sempre la chiamata corrente in attesa, e il completamento del trasferimento può avvenire mentre l'interno sta squillando o anche dopo la risposta
  - **Cieco/Senza Conferma**: Trasferisce immediatamente la chiamata corrente all'interno configurato

### Lingua e Localizzazione

- **Lingua Telefono**: Lingua utilizzata dallo schermo del telefono e dalla sua interfaccia web.

- **Suonerie**: Sono specifiche per ogni paese e indicano lo stato della chiamata attraverso un segnale udibile (tono libero, tono occupato, tono di riagganciamento, ecc.).

### Gestione Firmware

- **Firmware**: Caricamento e selezione di una nuova versione firmware per il telefono. Fare riferimento a [Phone Provisioning](./phone_provisioning.md#firmware-upgrade) per i dettagli sugli aggiornamenti firmware.

## Rubrica LDAP

La sezione Rubrica LDAP consente l'integrazione con servizi directory esterni.

### Tipo di Rubrica

Le prime due opzioni in **Tipo di Rubrica** non consentono ulteriori modifiche:
- I telefoni utilizzeranno la rubrica centralizzata fissa e non modificabile di NethVoice
- Selezionando "Rubrica personalizzata", è possibile modificare i campi rimanenti per collegare i telefoni a un server LDAP di terze parti

### Parametri di Configurazione LDAP

- **Indirizzo Server**: Nome host o indirizzo IP del server LDAP.

- **Numero Porta**: Porta TCP utilizzata dal server LDAP.

- **Nome Utente**: Nome utente di autenticazione per il servizio LDAP. Può essere specificato come Distinguished Name (DN) LDAP o in un altro formato a seconda dei requisiti del server LDAP.

- **Password**: Password di autenticazione per il servizio LDAP.

- **Crittografia**: Protegge la connessione con TLS o STARTTLS.
  :::warning
  Alcuni telefoni non supportano la crittografia. Se la connessione non riesce, selezionare "Nessuno".
  :::

- **Base di Ricerca (DN)**: Limita l'accesso al ramo del database LDAP specificato come base. Di solito, la base di ricerca è obbligatoria.

- **Filtro di Ricerca per Nome Contatto**: Filtro di ricerca LDAP per il recupero dei nomi dei contatti. Deve seguire la sintassi RFC-4515. Usa `%` come segnaposto per il termine di ricerca.

- **Filtro di Ricerca per Numero Telefono**: Filtro di ricerca LDAP per il recupero dei numeri di telefono. Deve seguire la sintassi RFC-4515. Usa `%` come segnaposto per il numero di telefono.

- **Attributi per Nome Contatto**: Separati da spazio, elenca i nomi degli attributi LDAP che possono contenere il nome del contatto.

- **Formato di Visualizzazione Nome**: I nomi degli attributi preceduti da `%` possono essere composti per formare il pattern con cui il nome è visualizzato sullo schermo del telefono.

- **Attributo per Numero Telefono Principale**: Attributo LDAP contenente il numero di telefono principale.

- **Attributo per Numero Mobile**: Attributo LDAP contenente il numero di telefono cellulare.

- **Attributo per Altro Numero Telefono**: Attributo LDAP contenente altri numeri di telefono.

## Rete

Questa sezione configura i parametri a livello di rete per il telefono.

### Configurazione DHCP

I telefoni utilizzano il protocollo DHCP per ricevere la configurazione di rete: indirizzo IP, subnet mask, DNS e gateway. In alcuni casi, DHCP viene utilizzato anche per ottenere l'URL di provisioning (fare riferimento a [Metodi di Provisioning](./phone_provisioning.md#provisioning-methods)).

### Configurazione VLAN

I seguenti parametri possono essere configurati per il supporto VLAN:

- **Identificatore VLAN (VID)**: Specificando un numero tra 1 e 4094, il telefono aggiungerà tagging VLAN ai pacchetti generati dal telefono stesso, in conformità allo standard IEEE 802.1Q.

- **Identificatore VLAN per Porta PC**: Specificando un numero tra 1 e 4094, il telefono aggiungerà tagging VLAN ai pacchetti provenienti dalla porta PC (o porta dati), seguendo lo standard IEEE 802.1Q.

:::warning
L'inserimento di un identificatore VLAN non corretto può rendere il telefono irraggiungibile. Testare attentamente le configurazioni VLAN.
:::

### Valori dei Campi VLAN

Nei campi VLAN:
- Stringa vuota `""` generalmente considera l'impostazione con priorità inferiore (modello o predefinito)
- `"0"` (zero) corrisponde a "disabilitato"

---

## Best Practices per Parametri di Provisioning

1. **Testare in Sviluppo**: Testare sempre le configurazioni dei parametri su un telefono non-produzione prima di distribuire ai dispositivi di produzione.

2. **Utilizzare la Gerarchia in Modo Efficace**: Sfruttare la priorità di configurazione per impostare i predefiniti e quindi personalizzare i singoli telefoni secondo le necessità.

3. **Documentare le Configurazioni Personalizzate**: Documentare eventuali tasti soft, tasti linea o configurazioni LDAP personalizzate per riferimento futuro e risoluzione dei problemi.

4. **Convalidare le Impostazioni di Rete**: Assicurarsi che le impostazioni DHCP e VLAN siano corrette prima del provisioning per evitare problemi di connettività.

5. **Monitorare il Provisioning**: Controllare i log di provisioning per verificare che i telefoni stiano ricevendo e applicando le configurazioni correttamente.
