---
title: Dashboard
sidebar_position: 11
---

# Dashboard

Il Dashboard funge da pagina iniziale di NethVoice dopo la prima configurazione. Offre una panoramica completa degli elementi coinvolti nell'operazione di NethVoice, fornendo agli amministratori informazioni in tempo reale sullo stato del sistema e l'attività degli utenti.

## Utenti

La sezione Utenti del Dashboard mostra tutti gli utenti configurati in NethVoice insieme al loro stato di presenza e ai dispositivi telefonici associati.

### Stato di presenza

Lo stato di presenza attuale di ogni utente è visualizzato, che può includere:

- **Disponibile**: L'utente è pronto per ricevere chiamate
- **Non disturbare (DND)**: L'utente ha abilitato DND e non riceverà chiamate
- **Assente**: L'utente è temporaneamente non disponibile
- **Offline**: L'utente non è registrato o connesso

### Ripristino dello stato di presenza

Se la configurazione della presenza di un utente si discosta dallo stato previsto, puoi ripristinarla allo stato predefinito "Disponibile" facendo clic sul simbolo di cancellazione/ripristino accanto al suo nome. Questo è utile quando lo stato di presenza rimane bloccato a causa di problemi tecnici o disconnessioni impreviste.

### Dettagli del dispositivo

Facendo clic per visualizzare i dettagli su un singolo dispositivo vengono visualizzate le seguenti informazioni del dispositivo telefonico:

| Proprietà | Descrizione |
|----------|-------------|
| **Nome** | L'identificativo del dispositivo o il soprannome |
| **Modello** | Il modello del telefono o il tipo di dispositivo |
| **Indirizzo IP** | L'indirizzo IP corrente del dispositivo; facendo clic facilita la connessione diretta sulla rete locale |
| **Porta SIP** | La porta su cui il dispositivo è registrato tramite SIP |
| **Codec utilizzati** | I codec audio attualmente in uso dal dispositivo |
| **DND (Non disturbare)** | Stato DND corrente del dispositivo |
| **Inoltro di chiamata** | Qualsiasi configurazione di inoltro di chiamata attiva per il dispositivo |

Questa visualizzazione dettagliata aiuta gli amministratori a risolvere i problemi di connettività del dispositivo e a monitorare le configurazioni specifiche del dispositivo.

## Trunk

La sezione Trunk visualizza tutti i trunk VoIP configurati in NethVoice insieme al loro stato operativo. Ogni voce trunk mostra:

| Proprietà | Descrizione |
|----------|-------------|
| **Nome** | L'identificativo o il nome del trunk |
| **Tecnologia** | Il protocollo utilizzato (ad es. SIP, PRI, ISDN) |
| **Indirizzo IP** | L'indirizzo IP dell'endpoint del trunk |
| **Porta** | Il numero di porta utilizzato per la connessione del trunk |
| **Stato** | Stato operativo attuale (ad es. Online, Offline, Errore) |
| **Codec** | I codec audio supportati da questo trunk |

### Monitoraggio dello stato dei trunk

Il monitoraggio regolare dello stato dei trunk dal Dashboard garantisce:

- Connettività alle chiamate esterne
- Rilevamento tempestivo dei problemi di connessione
- Verifica della qualità del servizio (QoS)
- Bilanciamento del carico su più trunk

:::tip
Se un trunk viene visualizzato come offline o con errori, verifica la configurazione del trunk nella Procedura guidata e assicurati che le credenziali del provider e i parametri di connessione siano corretti.
:::

## Panoramica del sistema in tempo reale

Il Dashboard fornisce una rappresentazione visiva rapida di:

- Salute e disponibilità del sistema
- Utenti attivi e il loro stato
- Dispositivi connessi e stato di registrazione
- Disponibilità e prestazioni del trunk
- Stato operativo complessivo del PBX

Questo rende il Dashboard uno strumento essenziale per l'amministrazione quotidiana e il monitoraggio del tuo sistema NethVoice.

:::note
Il Dashboard viene automaticamente aggiornato periodicamente. La velocità di aggiornamento può in genere essere configurata nella sezione Preferenze se necessario.
:::
