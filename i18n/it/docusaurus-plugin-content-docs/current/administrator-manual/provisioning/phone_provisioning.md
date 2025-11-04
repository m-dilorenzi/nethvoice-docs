---
title: Phone provisioning
sidebar_position: 2
---

# Provisioning Telefonico

Il provisioning implica la configurazione automatica dei telefoni, minimizzando le operazioni necessarie.

Azioni da eseguire in NethVoice:

1. Identificazione dei telefoni.
2. Assegnazione dei telefoni agli utenti.

## Telefoni Supportati

Vedere [telefoni supportati](supported_phones) per un elenco di telefoni supportati e le loro versioni firmware.


## Identificazione dei Telefoni

L'indirizzo MAC è fondamentale per il **Provisioning** di NethVoice in quanto identifica univocamente il telefono.

L'inserimento dell'indirizzo MAC dei telefoni non richiede il collegamento del telefono alla rete. Infatti, è possibile inserire gli indirizzi MAC di telefoni ancora imballati.

In ogni caso, è possibile inserire gli indirizzi MAC dei telefoni digitandoli o copiandoli da un foglio di calcolo, una fattura o altro documento.

## Associazione dei Telefoni agli Utenti

La configurazione di un telefono è completa quando è associata a un utente.

Fino a otto dispositivi telefonici possono essere associati a ciascun utente.

NethVoice assegna un numero progressivo a ogni dispositivo associato all'utente utilizzando i seguenti criteri:

- `Internal Principale` - telefono principale, ad esempio, `201`

- `91+Internal Principale` - telefono 2, ad esempio, `91201`

- `92+Internal Principale` - telefono 3, ad esempio, `92201`

- ...

Tuttavia, dal punto di vista dell'utente, l'Internal Principale è l'unico numero importante da ricordare.

## Azioni da Eseguire sui Telefoni

:::note
Considerare l'**accensione iniziale** per telefoni nuovi, appena tolti dalla scatola, o quelli che hanno subito un ripristino alle impostazioni di fabbrica e non sono mai stati avviati.
:::

I telefoni all'**accensione iniziale** sono già in grado di raggiungere NethVoice per recuperare la loro configurazione utilizzando i metodi supportati.

L'unica azione richiesta in questi casi è collegare il cavo Ethernet con PoE (Power over Ethernet) al telefono. Se PoE non è disponibile, sarà necessario collegare anche il cavo di alimentazione del telefono.

:::warning
Verificare la compatibilità dei telefoni con i metodi di provisioning supportati. Si prega di leggere attentamente le seguenti sezioni.
:::

Se un telefono è già in uso, è possibile prepararlo per l'associazione con NethVoice attraverso le procedure di **aggiornamento firmware** e **ripristino alle impostazioni di fabbrica**. Entrambe le procedure sono accessibili tramite l'interfaccia di amministrazione web del telefono.


## Metodi di Provisioning {#provisioning-methods}

I telefoni possono accedere alla loro configurazione tramite protocolli web standard, HTTP o HTTPS (porta TCP 80 o 443).

Quando l'indirizzo MAC del telefono viene inserito in NethVoice, viene generato un URL di provisioning (indirizzo).

Per esempio:

```
https://NethVoiceBaseHost/provisioning/1234567890.1234/{mac}.cfg
```

Questo URL contiene un segreto (`1234567890.1234` nell'esempio) che autentica e identifica il dispositivo che lo utilizzerà.

Per ottenere l'URL di provisioning, il telefono, all'accensione iniziale, può utilizzare due metodi: **RPS** e **DHCP**.

Il metodo **RPS** (Redirect & Provisioning Service) implica l'inserimento dell'URL di provisioning sul sito web del produttore del telefono. NethVoice è in grado di eseguire questo inserimento automaticamente. Non appena il telefono viene acceso per la prima volta, tenta di contattare il sito web del produttore per ottenere l'URL di provisioning.

Il metodo **DHCP** si basa sulla configurazione di OPTION 66 del protocollo DHCP (Dynamic Host Configuration Protocol) specificamente per ogni marca di telefono. È necessario configurare appropriatamente il server DHCP della rete.

Se né RPS né DHCP funzionano, è possibile accedere all'interfaccia web dell'amministrazione del telefono e inserire manualmente l'URL di provisioning. Ricordarsi di disabilitare altri metodi di provisioning, come DHCP e PNP.

L'URL di provisioning è visualizzato nell'interfaccia di amministrazione di NethVoice per ogni telefono, tramite il pulsante `Info` nella pagina `Dispositivi > Telefoni`.

In ogni caso, una volta ottenuto l'URL di provisioning, il telefono lo utilizza sempre per accedere alla sua configurazione su NethVoice.

:::warning
Fare riferimento alla sezione `provisioning-support-section` per ulteriori informazioni sul supporto del produttore per RPS e DHCP.
:::

## Specifiche di Configurazione del Telefono

Se si desidera modificare o personalizzare le impostazioni dei telefoni configurati tramite provisioning, accedere all'interfaccia di amministrazione web di NethVoice, modificando le impostazioni al livello *Predefinito*, *Modello* o *telefono individuale*.

### Priorità di Configurazione del Telefono {#phone-configuration-priority}

La configurazione del telefono segue una struttura gerarchica in cui le impostazioni possono essere definite a tre livelli:

1. **Livello Telefono** (Priorità Più Alta) - Impostazioni del singolo telefono
2. **Livello Modello** (Priorità Media) - Impostazioni applicate a tutti i telefoni di un modello specifico
3. **Livello Predefinito** (Priorità Più Bassa) - Impostazioni predefinite globali per tutti i telefoni

Quando un parametro viene lasciato vuoto o impostato su `-` (segno meno) a un livello di priorità più alta, il telefono erediterà il valore dal livello di priorità successivo. Questa gerarchia consente di impostare predefiniti ampi e quindi personalizzare modelli specifici o singoli telefoni secondo necessità.

I parametri modificabili includono:

- Lingua
- Fuso orario
- Formato data/ora
- Toni
- Password amministratore
- Avviso di chiamata
- Suoneria
- Modalità trasferimento
- Rubrica LDAP
- VLAN
- Tasti soft
- Tasti linea
- Tasti di espansione
- Screen Saver e Sfondo

Fare riferimento a `wizard-section` per ulteriori informazioni.

:::warning
Non modificare le impostazioni dall'interfaccia di amministrazione del telefono.
:::

Al riavvio, il telefono recupera le configurazioni dall'URL di provisioning.

Tutte le modifiche apportate dall'interfaccia di amministrazione del telefono andranno perse.

Le seguenti sezioni descrivono alcune impostazioni fornite da NethVoice.

I telefoni sottoposti a provisioning aggiorneranno automaticamente la loro configurazione anche in caso di cambio di stato (Disponibile, Non Disturbare, ecc.) in NethVoice CTI dell'utente connesso per mantenere l'uniformità dello stato su tutti i dispositivi.

Questo aggiornamento della configurazione non causa alcun disturbo o riavvio del telefono.

## Password Amministratore

L'interfaccia di amministrazione web del telefono è accessibile con il nome utente `admin` e una password generata casualmente durante l'installazione di NethVoice.

La password è disponibile nell'interfaccia di amministrazione di NethVoice, nella pagina `Modelli > Impostazioni Predefinite`.



## Aggiornamenti Automatici

Il telefono contatta automaticamente NethVoice ogni notte per aggiornare la sua configurazione. È possibile disabilitare completamente gli aggiornamenti automatici.

In ogni caso, il telefono scarica la configurazione ogni volta che viene riavviato.



## Aggiornamento Firmware {#firmware-upgrade}

Il produttore del telefono pubblica periodicamente aggiornamenti firmware per i vari modelli dei loro telefoni sul loro sito web.

È possibile distribuire il firmware aggiornato a tutti i telefoni dello stesso modello o a un singolo telefono.
Il file firmware ottenuto dal sito web del produttore deve essere caricato tramite l'interfaccia di amministrazione di NethVoice, rispettivamente in `Modelli > Preferenze > Firmware` o in `Configurazione > Dispositivi Associati > Modifica > Preferenze`.

Il nome del file può contenere solo lettere, numeri e i simboli `._-()`.

I telefoni ricevono l'aggiornamento secondo i tempi indicati in `provisioning-automatic-updates`.

:::tip
Quando i telefoni hanno ricevuto l'aggiornamento, deselezionare il file firmware nell'interfaccia NethVoice per ridurre il traffico di rete.
:::

Elenco di pagine web per il download del firmware:

- [Yealink](http://support.yealink.com/documentFront/forwardToDocumentFrontDisplayPage)
- [Snom](https://service.snom.com/display/wiki/Firmware+Update+Center)
- [Fanvil](https://fanvil.com/Support/download.html)
- [Gigaset](https://teamwork.gigaset.com/gigawiki/pages/viewpage.action?pageId=37486876)

