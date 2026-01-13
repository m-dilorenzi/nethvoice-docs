---
title: Installazione di NethVoice
sidebar_position: 4
---

# Installazione di NethVoice

NethVoice è un'applicazione VoIP che richiede un'installazione specifica su NethServer. Questa guida ti accompagnerà nel processo di installazione.

:::tip
Se desideri un'installazione di NethVoice pronta all'uso, prendi in considerazione:
- il nostro servizio **[NethVoice SaaS](saas.md#nethvoice-as-a-service)**, che fornisce un'istanza NethVoice completamente gestita nel cloud
- un **[VoiceBox Appliance](voicebox.md)**, l'appliance hardware con NethServer e NethVoice preinstallati
:::

## Panoramica

NethVoice è installato in due passaggi:

1. **NethVoice Proxy** (richiesto per primo)
2. **Modulo/i NethVoice**

NethVoice Proxy è un componente obbligatorio che deve essere installato e configurato **prima** di distribuire istanze di NethVoice. Ciò si applica anche se stai installando solo una singola istanza di NethVoice.

:::warning Ordine di installazione
**NethVoice Proxy deve essere installato PER PRIMO, prima di NethVoice.**

Il proxy gestisce tutto l'accesso a Internet esterno e gestisce l'instradamento del traffico SIP/RTP. È richiesto per:
- Accesso esterno da Internet
- Delega del traffico a più installazioni di NethVoice sullo stesso nodo
- Gestione dei collegamenti SIP e RTP per tutte le istanze di NethVoice
- Terminazione SSL/TLS per il traffico VoIP esposto a Internet

Anche con una singola installazione di NethVoice, il proxy è essenziale per una corretta gestione del traffico di rete.
:::

## Passaggi di installazione

### Passaggio 1: Installa NethVoice Proxy

1. **Accedi al Software Center** nel tuo sistema NethServer 8.
2. **Cerca "NethVoice Proxy"** nella barra di ricerca del Software Center.
3. **Fai clic su "Installa"** accanto a NethVoice Proxy.
4. **Attendi il completamento dell'installazione** (potrebbe richiedere alcuni minuti).
5. **Procedi alla configurazione del proxy** prima di passare al passaggio successivo (vedi [Configurazione di NethVoice Proxy](#step-2-configure-nethvoice-proxy)).

:::tip Importante
Assicurati che NethVoice Proxy sia completamente installato e configurato con FQDN appropriate e record DNS prima di procedere all'installazione delle istanze di NethVoice.
:::

### Passaggio 2: Configura NethVoice Proxy {#step-2-configure-nethvoice-proxy}

Prima di installare NethVoice, devi configurare NethVoice Proxy:

1. **Configura il dominio proxy** questo è l'FQDN pubblico dove il proxy sarà raggiungibile.
   Non inserire l'FQDN di NethServer ma utilizzarne uno dedicato, come `proxy.nethserver.org`.
   Questo nome verrà utilizzato dai client esterni per raggiungere i tuoi servizi VoIP, ma
   non verrà utilizzato direttamente dagli utenti finali.
2. **Imposta l'interfaccia di rete** che gestirà il traffico VoIP
3. **Configura l'indirizzo IP pubblico** se diverso dall'IP dell'interfaccia

La configurazione precedente sarà il punto di ingresso per tutto il traffico VoIP esterno.

Assicurati che:
- l'FQDN configurato si risolva correttamente all'indirizzo IP pubblico
- eventuali record DNS siano configurati correttamente per puntare al proxy

Questi requisiti sono critici per ottenere un certificato SSL/TLS valido per le comunicazioni sicure.

Vedi [Documentazione di NethVoice Proxy](../advanced/nethvoice_proxy.md) per ulteriori informazioni.

### Passaggio 3: Installa NethVoice

Una volta che NethVoice Proxy è in esecuzione, puoi installare le istanze di NethVoice:

1. **Torna al Software Center** nel tuo sistema NethServer 8.
2. **Cerca "NethVoice"** nella barra di ricerca del Software Center.
3. **Fai clic su "Installa"** accanto a NethVoice.
4. **Attendi il completamento dell'installazione**.
5. **Procedi con la configurazione del modulo** come descritto nella sezione successiva.
6. **Accedi all'istanza di NethVoice** e segui la procedura guidata di configurazione iniziale per completare la configurazione.

:::info Più istanze
Puoi installare più istanze di NethVoice sullo stesso nodo. Ognuna utilizzerà il NethVoice Proxy condiviso per l'accesso esterno e l'instradamento del traffico. Ogni istanza richiede una configurazione separata e FQDN dedicati.
:::

## Configurazione del modulo {#module-configuration}

:::warning Prerequisiti richiesti
Prima di procedere con la configurazione di qualsiasi istanza di NethVoice, assicurati che:

1. **NethVoice Proxy sia installato** - Vedi [Installazione di NethVoice Proxy](../advanced/nethvoice_proxy.md)
2. **NethVoice Proxy sia configurato** - Il dominio proxy (FQDN) deve essere impostato e i record DNS creati
3. **NethVoice Proxy sia in esecuzione** - Verifica lo stato del proxy nell'interfaccia di gestione del nodo
4. **Il dominio utente sia creato** - Vedi [Domini utente nell'installazione di NethServer](./nethserver.md#user-domains) (richiesto per gli utenti e gli interni di NethVoice)

Il modulo NethVoice richiede almeno un dominio utente per gestire utenti, interni e autenticazione. Se non hai ancora creato un dominio utente, segui la [guida alla configurazione dei domini utente](./nethserver.md#user-domains) prima di configurare NethVoice.
:::

Per configurare NethVoice, hai bisogno di due host virtuali dedicati:

- uno per la pagina di amministrazione di NethVoice, ad es. `nethvoice.nethserver.org`
- uno per l'applicazione web NethVoice CTI, ad es. `cti.nethserver.org`

Prima di procedere con la configurazione, assicurati di aver creato i record DNS corrispondenti per questi FQDN nel tuo server DNS.

Se prevedi di utilizzare un certificato Let's Encrypt come certificato predefinito, assicurati di avere i necessari record DNS pubblici.

Durante la procedura guidata di configurazione del modulo, ti verrà chiesto di fornire le seguenti informazioni:

- **Host base di NethVoice**: Inserisci un FQDN valido per accedere alla pagina di amministrazione dell'applicazione, qui è dove gestirai le impostazioni di NethVoice, ad es. `nethvoice.nethserver.org`.
- **Host base di NethVoice CTI**: Inserisci un FQDN valido per accedere all'applicazione web NethVoice CTI, ad es. `cti.nethserver.org`.
- **Dominio utente**: Scegli uno dei [domini utente](./nethserver.md#user-domains) già configurati.
- **Fuso orario**: Seleziona il fuso orario appropriato per la tua istanza di NethVoice, questo è importante per la registrazione e la pianificazione accurate delle chiamate.
- **Richiedi certificato Let's Encrypt**: Se abilitato, verrà richiesto un certificato Let's Encrypt per ognuno dei due host.
- **Prefisso report**: Inserisci il prefisso telefonico internazionale da considerare locale nel sistema di reporting.
- **Ripristina la password dell'amministratore di NethVoice per accedere all'interfaccia utente**: Inserisci una password valida per l'utente amministratore di NethVoice (facoltativo, la password predefinita è *Nethesis,1234*).

Opzioni di configurazione avanzata:

- **Chiave API di Deepgram**: Inserisci la tua chiave API di Deepgram per abilitare funzionalità di riconoscimento vocale avanzate e trascrizione vocale.
  - **Abilita trascrizione delle chiamate**: Abilita questa opzione per permettere agli utenti di trascrivere le chiamate in tempo reale utilizzando il servizio speech-to-text di Deepgram. Questa funzione comporta costi aggiuntivi in base al tuo utilizzo di Deepgram.
  - **Trascrizione della segreteria telefonica**: Abilita la trascrizione della segreteria telefonica per convertire i messaggi della segreteria telefonica in testo utilizzando Deepgram. Questa funzione comporta anche costi aggiuntivi in base al tuo utilizzo di Deepgram.

:::info Trascrizione vocale
Per informazioni dettagliate su come gli utenti possono accedere e utilizzare le funzionalità di trascrizione vocale, vedi [Trascrizione Vocale](../../user-manual/nethcti/other.md#voice-transcription) nel Manuale Utente.
:::

Le seguenti opzioni sono disponibili solo con un abbonamento Enterprise attivo:

- **Abilita modulo hotel**: Attiva il modulo Hotel per la gestione delle funzionalità telefoniche specifiche dell'hotel.
  Vedi [Documentazione del modulo NethVoice Hotel](../nethhotel/index.md) per ulteriori dettagli.
- **Host del server Hotel FIAS**: Inserisci l'indirizzo IP o il nome host del server Hotel FIAS.
- **Porta del server Hotel FIAS**: Specifica il numero di porta per la connessione al server Hotel FIAS.

## Passaggi successivi

Dopo aver salvato i parametri di configurazione, NethVoice sarà accessibile al suo host base, ad es:
```
https://nethvoice.nethserver.org
```

Per accedere all'interfaccia di amministrazione di NethVoice, utilizza le seguenti credenziali:

- Utente: `admin`
- Password: `Nethesis,1234`, la password predefinita se l'opzione *Ripristina la password dell'amministratore di NethVoice per accedere all'interfaccia utente* non è stata utilizzata durante la configurazione

## Installazione del modulo {#installazione-del-modulo}

1. **Accedi al Software Center** sul tuo sistema NethServer 8.  
2. **Cerca "NethVoice"** nella barra di ricerca del Software Center.  
3. **Fai clic su "Installa"** accanto a NethVoice.  
4. **Attendi il completamento dell'installazione** (potrebbero essere necessari alcuni minuti).  

## Procedura guidata di configurazione iniziale {#procedura-guidata-di-configurazione}

Apri l'applicazione NethVoice dalla **pagina Applicazioni** o dal **Cassetto delle applicazioni** in NethServer 8. Apparirà una procedura guidata di configurazione iniziale che ti guiderà attraverso:  
- Configurazione di un provider di account per NethVoice  
- Installazione e configurazione del Proxy NethVoice  
- Configurazione dell'applicazione NethVoice  

### Provider di account {#provider-di-account}

Il primo passaggio della procedura guidata ti aiuta a configurare il dominio utenti utilizzato da NethVoice.  

I domini utenti memorizzano utenti e gruppi in un database LDAP. NethVoice richiede un dominio utenti per gestire interni, utenti e autenticazione.  
NethServer 8 supporta due tipi di provider di account LDAP:  

| Provider | Tipo | Ideale per | Funzionalità |
|----------|------|------------|--------------|
| **OpenLDAP (RFC2307)** | Interno | Client Unix/Linux, configurazione semplice | Leggero, configurazione semplice, distribuzioni di piccole dimensioni, istanze multiple per nodo |
| **Active Directory (Samba)** | Interno | Client Windows, condivisione file SMB | Controller di dominio, compatibilità Windows, maggiore complessità, una sola istanza per nodo |
| **LDAP Esterno** | Esterno | Infrastruttura LDAP esistente | Connessione a server esistenti (Active Directory, OpenLDAP, ecc.) |

:::info Requisiti di NethVoice  
NethVoice richiede almeno un dominio utenti configurato. Scegli **OpenLDAP (RFC2307)** per distribuzioni più semplici o **Active Directory** se hai bisogno di supporto per client Windows.  
:::

#### Configurazione rapida: OpenLDAP (Consigliato per NethVoice) {#configurazione-rapida-openldap-consigliato-per-nethvoice}

La procedura guidata consente di installare facilmente un provider di account OpenLDAP. Per configurarlo, devi:  

- **Inserire il nome del dominio** (es. `nethvoice.local`) - questo è un nome logico, non correlato al DNS  
- **Impostare nome utente e password dell'amministratore di OpenLDAP**  

Per scenari avanzati (LDAP esterno, Active Directory, configurazione DNS, politiche di password, gestione utenti), consulta la [documentazione ufficiale sui domini utenti di NethServer 8](https://docs.nethserver.org/projects/ns8/en/latest/user_domains.htm).  

Argomenti chiave nella documentazione ufficiale:  
- **Configurazione di Active Directory**: Configurazione completa del controller di dominio  
- **Connessione LDAP esterno**: Collegamento a server LDAP esistenti  
- **Politiche di password**: Età, complessità e scadenza delle password  
- **Portale di gestione utenti**: Modifica autonoma delle password da parte degli utenti  
- **Repliche del provider LDAP**: Tolleranza ai guasti e ridondanza  
- **Impostazioni di binding LDAP**: Collegamento di applicazioni esterne a un server LDAP locale  

### Proxy NethVoice {#proxy-nethvoice}

Il passaggio successivo della procedura guidata iniziale installa e configura il Proxy NethVoice.  

Il Proxy NethVoice è un componente che deve essere installato e configurato prima di distribuire le istanze dell'applicazione NethVoice. Anche con una sola installazione di NethVoice, il proxy è essenziale per una corretta gestione del traffico di rete.  

Il proxy gestisce tutto l'accesso esterno a Internet e il routing del traffico SIP/RTP. È necessario per:  
- Accesso esterno da Internet  
- Gestione delle connessioni SIP e RTP per tutte le istanze di NethVoice  
- Terminazione SSL/TLS per il traffico VoIP esposto a Internet  

Il Proxy NethVoice è un'applicazione standard di NethServer 8: le sue impostazioni possono essere riviste e modificate accedendo dal **Cassetto delle applicazioni** o dalla **pagina Applicazioni**.  

#### Prerequisiti {#prerequisiti}

Prima di configurare il Proxy NethVoice, assicurati che:  

1. **Record DNS creati**: Crea un record DNS A/AAAA per il dominio del proxy (es. `proxy.nethserver.org`) che punti al tuo indirizzo IP pubblico  
2. **Indirizzo IP pubblico**: Conosci l'indirizzo IPv4 o IPv6 pubblico dove il proxy sarà accessibile da Internet  
3. **Interfaccia di rete**: Identifica quale interfaccia di rete gestirà il traffico VoIP  

La procedura guidata rileva automaticamente se esiste già un proxy sul nodo di installazione di NethVoice e propone di installarlo se necessario. Successivamente, per configurare il Proxy NethVoice:  

1. **Configura il dominio del Proxy**: questo è il FQDN pubblico dove il proxy sarà raggiungibile.  
   Non inserire il FQDN di NethServer ma utilizza uno dedicato, come `proxy.nethserver.org`.  
   Questo nome sarà utilizzato dai client esterni per raggiungere i tuoi servizi VoIP, ma non sarà utilizzato direttamente dagli utenti finali.  
2. **Abilita la richiesta del certificato Let's Encrypt** se necessario: verrà richiesto un certificato Let's Encrypt per il dominio del proxy.  
3. **Imposta l'interfaccia di rete** che gestirà il traffico VoIP  
4. **Configura l'indirizzo IP pubblico** se diverso dall'IP dell'interfaccia  

La configurazione sopra sarà il punto di ingresso per tutto il traffico VoIP esterno.  

Assicurati che:  
- Il FQDN configurato risolva correttamente l'indirizzo IP pubblico  
- Eventuali record DNS siano correttamente configurati per puntare al proxy  

Questi requisiti sono fondamentali per ottenere un certificato SSL/TLS valido per comunicazioni sicure.  

Consulta la [documentazione del Proxy NethVoice](../advanced/nethvoice_proxy.md) per maggiori informazioni.  

### Applicazione NethVoice {#applicazione-nethvoice}

:::warning Configurazione DNS  
Per configurare NethVoice, è necessario disporre di due virtual host dedicati:  

- Un **host base NethVoice** per l'interfaccia di amministrazione di NethVoice, ad esempio `nethvoice.nethserver.org`  
- Un **host base CTI NethVoice** per l'applicazione web CTI di NethVoice, ad esempio `cti.nethserver.org`  

Prima di procedere con la configurazione, assicurati di aver creato i corrispondenti record DNS per questi FQDN nel tuo server DNS.  

Se prevedi di utilizzare un certificato Let's Encrypt come certificato predefinito, assicurati di avere i necessari record DNS pubblici.  
:::

Nell'ultimo passaggio della procedura guidata, ti verrà richiesto di fornire le seguenti informazioni:  

- **Host base NethVoice**: Inserisci un FQDN valido per accedere alla pagina di amministrazione dell'applicazione; qui gestirai le impostazioni di NethVoice, ad esempio `nethvoice.nethserver.org`.  
- **Host base CTI NethVoice**: Inserisci un FQDN valido per l'applicazione web CTI di NethVoice, ad esempio `cti.nethserver.org`.  
- **Richiedi certificato Let's Encrypt**: Se abilitato, verrà richiesto un certificato Let's Encrypt sia per l'**host base NethVoice** che per l'**host base CTI NethVoice**.  
- **Fuso orario**: Seleziona il fuso orario appropriato per l'applicazione NethVoice; questo è importante per la registrazione accurata delle chiamate e la pianificazione.  
- **Password amministratore per accedere all'interfaccia utente**: Imposta la password per la pagina di amministrazione di NethVoice.  

### Passaggi successivi {#passaggi-successivi}

Al termine della procedura guidata di configurazione iniziale, NethVoice sarà accessibile sull'host base configurato, ad esempio:  
```
https://nethvoice.nethserver.org  
```  

Per accedere all'interfaccia di amministrazione di NethVoice, utilizza le seguenti credenziali:  

- Utente: `admin`  
- Password: La password scelta nella procedura guidata di configurazione iniziale  

Dopo aver completato la configurazione di NethVoice nell'interfaccia di amministrazione, gli utenti possono accedere al CTI di NethVoice sull'host base configurato, ad esempio:  
```
https://cti.nethserver.org  
```  

## Configurazione del modulo {#configurazione-del-modulo}

Le impostazioni del modulo NethVoice possono essere riviste e modificate accedendo al modulo NethVoice di NethServer 8. Per farlo:  

- Accedi alla pagina di amministrazione del cluster NethServer.  
- Apri l'applicazione NethVoice dal **Cassetto delle applicazioni** o dalla **pagina Applicazioni**.  
- Vai alla pagina di configurazione specifica che desideri modificare.  

Nella pagina **Impostazioni** puoi rivedere e modificare la maggior parte dei parametri di configurazione:  

- **Host base NethVoice**: virtual host per l'interfaccia di amministrazione di NethVoice.  
- **Host base CTI NethVoice**: virtual host per l'applicazione web CTI di NethVoice.  
- **Richiedi certificato Let's Encrypt**: se abilitato, verrà richiesto un certificato Let's Encrypt sia per l'**host base NethVoice** che per l'**host base CTI NethVoice**.  
- **Provider di account**: dominio utenti utilizzato da NethVoice.  
- **Fuso orario**: fuso orario per l'applicazione NethVoice, importante per la registrazione accurata delle chiamate e la pianificazione.  
- **Prefisso dei report**: prefisso telefonico utilizzato nei report.  
- **Nuova password amministratore per NethVoice**: definisci una nuova password per l'utente `admin`.  

Nella pagina **Integrazioni** puoi configurare la trascrizione di chiamate e messaggi vocali:  
- **Chiave API Deepgram**: Inserisci la tua chiave API Deepgram per abilitare funzionalità avanzate di riconoscimento vocale e trascrizione.  
- **Abilita trascrizione delle chiamate**: Abilita questa opzione per consentire agli utenti di trascrivere le chiamate in tempo reale utilizzando il servizio di conversione vocale in testo di Deepgram. Questa funzionalità comporta costi aggiuntivi in base all'utilizzo di Deepgram.  
- **Trascrizione dei messaggi vocali**: Abilita la trascrizione dei messaggi vocali per convertirli in testo utilizzando Deepgram. Anche questa funzionalità comporta costi aggiuntivi in base all'utilizzo di Deepgram.  

:::info Trascrizione vocale  
Per informazioni dettagliate su come gli utenti possono accedere e utilizzare le funzionalità di trascrizione vocale, consulta [Trascrizione vocale](../../user-manual/nethcti/other.md#voice-transcription) nel Manuale Utente.  
:::

Nella pagina **Rebranding** puoi personalizzare l'interfaccia utente di NethVoice con l'identità del marchio della tua azienda. Per abilitare questa funzionalità, devi contattare il team commerciale di Nethesis e avere un abbonamento Enterprise attivo.  

Nella pagina **Hotel** puoi configurare il modulo Hotel; è richiesto un abbonamento attivo per questa funzionalità.  

- **Stato**: Attiva il modulo Hotel per gestire funzionalità telefoniche specifiche per hotel.  
- **Host server FIAS Hotel**: Inserisci l'indirizzo IP o il nome host del server FIAS dell'hotel.  
- **Porta server FIAS Hotel**: Specifica il numero di porta per la connessione al server FIAS dell'hotel.  

Consulta la [documentazione del modulo Hotel di NethVoice](/docs/administrator-manual/nethhotel/index.md) per maggiori dettagli.