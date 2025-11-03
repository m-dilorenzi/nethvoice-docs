---
title: Integrazione FIAS
sidebar_position: 2
---

# Integrazione FIAS

L'integrazione FIAS (Fidelio Interface Application Specification) consente a NethHotel di connettersi con sistemi di gestione della proprietà (PMS) dell'hotel come Oracle Hospitality OPERA per la gestione agile degli ospiti e l'automazione della fatturazione.

## Panoramica

NethHotel può essere collegato a un sistema di gestione della proprietà (PMS) dell'hotel compatibile con il protocollo di scambio dati FIAS. **NethVoice è certificato da Oracle**, garantendo un'integrazione fluida con i sistemi Oracle Hospitality.

Collegando NethHotel a un PMS compatibile, le seguenti funzioni possono essere gestite direttamente dall'interfaccia PMS:

- **Check-in**: Attivazione automatica del telefono della camera al check-in dell'ospite
- **Check-out**: Disattivazione automatica del telefono della camera al check-out dell'ospite
- **Sveglia**: Programmazione e monitoraggio delle richieste di sveglia e rapporti di stato
- **Fatturazione**: Fatturazione automatica delle chiamate effettuate dalla camera
- **Fatturazione extra/minibar**: Fatturazione di articoli minibar e altri extra, incluso tramite codici funzionalità del telefono
- **Impostazioni della lingua**: Configurazione automatica della lingua del messaggio audio dell'ospite in base alla lingua della prenotazione

## Certificazione Oracle

NethVoice è stato certificato da Oracle per la compatibilità del protocollo FIAS, garantendo:

- Integrazione affidabile con i sistemi Oracle Hospitality
- Conformità agli standard del protocollo FIAS
- Supporto per i processi di flusso di lavoro standard di Oracle
- Verifica regolare della compatibilità con gli aggiornamenti di Oracle

## Versioni supportate

### Protocollo FIAS

| Componente | Versione |
|-----------|---------|
| **Protocollo FIAS** | Fidelio Interface Application Specification (FIAS) 2.20.23 |

### Componenti Oracle Hospitality

| Componente | Versione |
|-----------|---------|
| **Oracle Hospitality OPERA** | 5.5 |
| **Oracle Hospitality Interface IFC8** | 8.14.7.0 |

### Versioni minime richieste di Oracle PMS

Le seguenti sono le versioni minime richieste (anche le versioni superiori sono compatibili):

| Prodotto | Versione |
|---------|---------|
| **Opera 5 PMS** | V5.0.03.03 E43 |
| **Opera 5 PMS** | V5.0.04.01 E24 |
| **Opera 5 PMS** | V5.0.04.02 E17 |
| **Opera 5 PMS** | V5.0.04.03 E10 |

## Configurazione

### Abilitazione dell'integrazione FIAS

Per abilitare l'integrazione FIAS con la tua installazione di NethHotel:

1. Accedi alle applicazioni di NethVoice all'interno di NethServer
2. Vai alla pagina **Impostazioni**
3. Seleziona l'opzione **Abilita modulo hotel**
4. Inserisci l'**Host del server FIAS dell'hotel** (indirizzo IP o nome host del tuo PMS)
5. Inserisci la **Porta del server FIAS dell'hotel** (in genere la porta 7001 per Oracle OPERA)
6. Salva le modifiche

### Prerequisiti

Prima di configurare l'integrazione FIAS, assicurati che:

- Il tuo PMS dell'hotel sia installato e in esecuzione sull'host e sulla porta specificati
- Ci sia connettività di rete tra NethVoice e il tuo sistema PMS
- La versione del tuo PMS soddisfi le versioni minime richieste elencate sopra
- Le regole del firewall consentano la comunicazione tra NethVoice e il PMS sulla porta specificata
- Il protocollo FIAS sia abilitato nella configurazione del tuo PMS

## Sincronizzazione dei dati

Una volta abilitata l'integrazione FIAS, i sistemi sincronizzano i dati in tempo reale:

### Da PMS a NethVoice

- Il check-in dell'ospite attiva il telefono della camera
- Il check-out dell'ospite disattiva il telefono della camera
- Le preferenze di lingua dell'ospite vengono applicate ai telefoni della camera
- Le richieste di sveglia vengono elaborate

### Da NethVoice a PMS

- I record dei dettagli della chiamata (CDR) vengono inviati a scopo di fatturazione
- Gli addebiti extra (minibar, servizi) vengono registrati
- I rapporti di stato e completamento della sveglia vengono inviati
- Lo stato di disponibilità della camera viene aggiornato

## Vantaggi dell'integrazione FIAS

1. **Gestione automatica degli ospiti**: Elimina l'attivazione/disattivazione manuale del telefono della camera
