---
title: Installazione
sidebar_position: 1
---

# Guida all'installazione

Questa sezione copre il processo di installazione completo per NethVoice, dall'installazione dell'infrastruttura NethServer 8 sottostante alla configurazione di NethVoice stesso.

## Panoramica

L'installazione di NethVoice è un processo multi-passaggio:

1. **[Installazione di NethServer 8](nethserver.md)** - Installa la piattaforma base di NethServer 8
2. **[Crea dominio utente](nethserver.md#user-domains)** - Configura LDAP per utenti e autenticazione (in NethServer)
3. **[Installazione e configurazione di NethVoice Proxy](../advanced/nethvoice_proxy.md)** - Installa e configura il gateway VoIP esterno (RICHIESTO per primo)
4. **[Installazione di NethVoice](nethvoice_install.md)** - Installa NethVoice sopra il proxy configurato
5. **[Configurazione del modulo](nethvoice_install.md#module-configuration)** - Configura NethVoice con i tuoi requisiti

:::warning Ordine di installazione
1. NethServer 8 deve essere installato per primo
2. Il dominio utente deve essere creato per secondo (richiesto da NethVoice)
3. NethVoice Proxy deve essere installato e configurato per terzo
4. NethVoice può essere installato solo dopo che il proxy è pronto
5. La configurazione di NethVoice utilizza il dominio utente creato nel passaggio 2

Vedi [Installazione di NethVoice Proxy](../advanced/nethvoice_proxy.md) per i dettagli sui requisiti del proxy.
:::

## Cos'è NethServer 8?

NethServer 8 (NS8) è la piattaforma infrastruttura Linux sottostante su cui gira NethVoice. Fornisce:

- Gestione dell'infrastruttura Linux unificata open-source
- Supporto cluster per alta disponibilità e scalabilità
- Architettura dell'applicazione modulare
- Interfaccia di amministrazione basata su web
- Hardening della sicurezza e aggiornamenti

:::info
NethVoice richiede che NethServer 8 sia installato per primo. Assicurati di completare l'installazione di NethServer 8 prima di procedere con NethVoice.
:::

## Percorso di installazione

### Passaggio 1: Prerequisiti

Prima di iniziare, assicurati di avere:

- Una macchina fisica o virtuale dedicata
- Distribuzione Linux supportata installata (Rocky Linux, AlmaLinux, CentOS Stream o Debian)
- Indirizzo IP statico configurato
- Server DNS esterni configurati
- Connessione Internet funzionante
- Nome di dominio completamente qualificato (FQDN) registrato e risolto

### Passaggio 2: Installa NethServer 8

Segui la [guida all'installazione di NethServer](nethserver.md) per:
- Installare i componenti core di NethServer 8
- Configurare la rete e il DNS
- Accedere all'interfaccia di amministrazione web
- Creare il tuo cluster

### Passaggio 3: Crea dominio utente

Crea un dominio utente per gli utenti e gli interni di NethVoice:
- Accedi all'interfaccia web di NethServer 8 → Domini e utenti
- Crea dominio (OpenLDAP consigliato per NethVoice)
- Imposta le credenziali di amministrazione
- Annota le impostazioni di bind LDAP (necessarie per la configurazione di NethVoice)

Vedi [Setup dei domini utente](nethserver.md#user-domains) nella guida all'installazione di NethServer per i dettagli.

### Passaggio 4: Installa NethVoice Proxy

Dopo che NethServer 8 e il dominio utente sono pronti, installa e configura il proxy VoIP:
- Accedi al Software Center
- Installa NethVoice Proxy
- Configura il dominio proxy (FQDN)
- Imposta l'interfaccia di rete e l'IP pubblico
- Verifica che il proxy sia in esecuzione

Vedi [Guida all'installazione di NethVoice Proxy](../advanced/nethvoice_proxy.md) per i passaggi dettagliati.

### Passaggio 5: Installa NethVoice

Con NethVoice Proxy configurato e in esecuzione:
- Accedi al Software Center
- Installa NethVoice
- Completa la procedura guidata di configurazione di NethVoice
- Seleziona il dominio utente creato nel Passaggio 3
- Configura gli host virtuali e i certificati

### Passaggio 6: Configura NethVoice

Segui la [guida all'installazione di NethVoice](nethvoice_install.md) per:
- Configurare gli host virtuali di NethVoice
- Verificare che il dominio utente sia selezionato
- Configurare i certificati Let's Encrypt
- Accedere all'amministrazione e CTI di NethVoice

## Riferimento veloce

### Requisiti di sistema (Minimo)

| Componente | Requisito |
|-----------|-------------|
| CPU | 2 vCPU/core (x86-64) |
| RAM | 2GB |
| Archiviazione | 40GB SSD |
| Rete | Indirizzo IP statico |
| OS | **Rocky Linux 9** (subscription supportato) - AlmaLinux 9, CentOS Stream 9, Debian 12 (community supportato) |
| Browser | Firefox, Chrome o Chromium (versione attuale) |

### Metodi di installazione

**NethServer 8** può essere installato tramite:
- Script di installazione standard (consigliato)
- Immagine di macchina virtuale pre-costruita (per Proxmox o VMWare)

**NethVoice** è installato tramite:
- Interfaccia del Software Center di NethServer

### Credenziali predefinite

Dopo l'installazione, utilizza queste credenziali temporanee:

| Componente | Nome utente | Password |
|-----------|----------|----------|
| Interfaccia amministratore di NethServer 8 | admin | Nethesis,1234 |
| Interfaccia amministratore di NethVoice | admin | Nethesis,1234 |

:::warning
Cambia le credenziali predefinite immediatamente dopo il primo accesso per motivi di sicurezza.
:::

## Guide dettagliate

### [Installazione di NethServer 8](nethserver.md)

Guida completa che copre:
- Requisiti di sistema e consigli hardware
- Distribuzioni Linux supportate
- Configurazione di rete e DNS
- Procedura di installazione standard
- Distribuzione di immagini pre-costruite
- Passaggi post-installazione
- Configurazione del cluster
- Risoluzione dei problemi

### [Installazione di NethVoice Proxy](../advanced/nethvoice_proxy.md)

Guida completa che copre:
- Panoramica del proxy e architettura
- Ruolo nelle distribuzioni con una e più istanze
- Passaggi di installazione
- Configurazione (dominio, interfaccia, IP pubblico)
- Configurazione del certificato SSL
- Verifica e test
- Deve essere installato PRIMA di NethVoice

### [Installazione di NethVoice](nethvoice_install.md)

Guida completa che copre:
- Ordine di installazione (Proxy → NethVoice)
- Installazione software di NethVoice
- Configurazione del modulo
- Configurazione dell'host virtuale
- Configurazione del dominio utente
- Configurazione del certificato Let's Encrypt
- Accesso amministratore
- Configurazione iniziale

## Elenco di controllo dell'installazione

Prima di iniziare, assicurati che:

- [ ] L'hardware soddisfa i requisiti minimi (2 vCPU, 2GB RAM, 40GB SSD)
- [ ] Distribuzione Linux supportata disponibile
- [ ] Indirizzo IP statico configurato
- [ ] Server DNS esterni configurati
- [ ] FQDN registrato presso il provider DNS
- [ ] Il firewall consente le porte richieste (80, 443, 55820 per il clustering)
- [ ] La connessione Internet è stabile
- [ ] Hai accesso amministrativo al server

Durante l'installazione, assicurati di completare:

- [ ] Installazione di NethServer 8
- [ ] Creazione del dominio utente (OpenLDAP consigliato)
- [ ] Annota le impostazioni di bind LDAP
- [ ] Installazione di NethVoice Proxy
- [ ] Configurazione di NethVoice Proxy
- [ ] Verifica che il proxy sia in esecuzione prima dell'installazione di NethVoice
- [ ] Installazione di NethVoice
- [ ] Configurazione di NethVoice con il dominio utente

## Note importanti

:::info
**Solo piattaforme supportate**: Installa NethServer 8 solo su distribuzioni supportate. Sistemi desktop e server che eseguono altri servizi non sono supportati.
:::

:::info
**Indirizzo IP statico**: DHCP non è supportato. Configura un indirizzo IP statico prima o durante l'installazione di NethServer 8.
:::

:::warning
**Configurazione DNS**: Una corretta configurazione DNS è essenziale per i certificati TLS, il clustering e la funzionalità complessiva del sistema. Non saltare i passaggi di configurazione DNS.
:::

:::warning
**Credenziali predefinite**: Cambia le password amministratore predefinite immediatamente dopo l'installazione. Questo è un requisito di sicurezza, non facoltativo.
:::

## Scalabilità

Dopo l'installazione iniziale, NethServer 8 supporta:

- **Configurazione cluster**: Aggiungi più nodi per la scalabilità
- **Nodi worker**: Distribuisci applicazioni tra i nodi del cluster
- **Bilanciamento del carico**: Bilanciamento del carico integrato per le applicazioni
- **VPN**: Configurazione VPN automatica per la comunicazione sicura tra nodi

Vedi la [documentazione di NethServer 8](https://docs.nethserver.org/projects/ns8/) per i dettagli del clustering.

## Risoluzione dei problemi

### Problemi comuni

**Non è possibile accedere all'interfaccia web**
- Verifica la configurazione dell'indirizzo IP statico
- Controlla che il firewall consenta la porta 443
- Assicurati che il DNS risolva correttamente l'FQDN
- Vedi la guida all'installazione di NethServer 8

**Problemi di connettività di rete**
- Configura l'indirizzo IP statico
- Verifica che i server DNS siano raggiungibili e non locali
- Controlla la configurazione dell'interfaccia di rete
- Testa la risoluzione DNS da riga di comando

**Installazione dello script non riuscita**
- Assicurati che la connessione Internet sia stabile
- Installa curl se non disponibile
- Esegui come utente root
- Verifica che i requisiti di sistema siano soddisfatti

Per ulteriore aiuto, consulta le guide dettagliate o la documentazione di NethServer 8.

## Passaggi successivi

Dopo l'installazione completata con successo:

1. **Configura NethVoice**: Completa la procedura guidata di configurazione di NethVoice
2. **Configura utenti**: Crea domini utente (LDAP o Active Directory)
3. **Provisioning di telefoni**: Vedi la [guida al provisioning dei telefoni](../provisioning/index.md)
4. **Formazione utenti**: Utilizza il [Manuale utente](../../user-manual/index.md) per formare gli utenti finali
5. **Hardening della sicurezza**: Configura firewall e controlli di accesso

---

**Pronto per iniziare?** Inizia con la [guida all'installazione di NethServer 8](nethserver.md).
