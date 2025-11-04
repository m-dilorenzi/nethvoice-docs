---
title: Prerequisiti
sidebar_position: 1
---

# Prerequisiti

Prima di avviare la migrazione di NethVoice da NethServer 7 a NethServer 8, assicuratevi che tutti i prerequisiti siano soddisfatti. Una preparazione adeguata è essenziale per un processo di migrazione fluido.

## Requisiti di Sistema

### Sistema di Origine (NethServer 7)

Il vostro sistema NethServer 7 deve soddisfare i seguenti requisiti:

- **Accesso SSH**: Accesso SSH come root o amministratore al server NS7
- **Accesso Cockpit**: Accesso all'interfaccia web tramite Cockpit (normalmente sulla porta 9090)
- **NethVoice Operativo**: L'installazione di NethVoice deve essere in esecuzione e funzionante
- **Strumento di Migrazione**: Capacità di installare il modulo "Migration to NS8" da Software Center
- **Aggiornamenti di Sistema**: NS7 dovrebbe essere completamente aggiornato prima di avviare la migrazione

### Sistema di Destinazione (NethServer 8)

Il sistema NS8 di destinazione richiede:

- **Installazione Pulita**: Un cluster NS8 appena installato (vedere [Guida all'Installazione NS8](../../administrator-manual/install/nethserver.md))
- **Risorse Adeguate**: CPU, RAM e spazio su disco sufficienti per ospitare NethVoice e i suoi dati
  - Minimo: 4 vCPU, 8GB RAM, 100GB spazio disco
  - Consigliato: Scalare in base all'utilizzo e al volume di dati di NS7
- **Proxy NethVoice**: Dovrebbe essere pre-installato e configurato (vedere [Documentazione Proxy NethVoice](../../administrator-manual/advanced/nethvoice_proxy.md))
  - Nota: Se non installato, lo strumento di migrazione lo installerà automaticamente, ma la configurazione manuale sarà richiesta successivamente
- **Trunk VoIP e telefoni supportati**: Assicuratevi che tutti i trunk VoIP e i telefoni utilizzati in NS7 siano supportati in NS8. Controllate la documentazione [Telefoni Supportati](../../administrator-manual/provisioning/supported_phones.md), [Gateway Supportati](../../administrator-manual/provisioning/supported_gateways.md) e [Trunk supportati](../../administrator-manual/provisioning/supported_trunks.md) per informazioni sulla compatibilità.

:::tip Pre-installa Proxy NethVoice
Si consiglia vivamente di installare e configurare Proxy NethVoice **prima** di avviare la migrazione. Questo assicura una corretta configurazione di rete e riduce i compiti post-migrazione.
:::

## Requisiti di Rete

### Connettività VPN

Il cluster NS8 utilizza una VPN per la comunicazione sicura tra i nodi e durante la migrazione:

- **Risoluzione Indirizzo VPN**: L'indirizzo VPN del cluster NS8 deve essere risolvibile da NS7
  - L'indirizzo VPN è configurato durante la creazione del cluster
  - Per impostazione predefinita, questo è l'FQDN del nodo leader
- **Accesso Porta VPN**: La porta VPN predefinita **55820** non deve essere bloccata da:
  - Firewall su NS7 o NS8
  - Appliance di rete intermedie
  - ACL del router tra NS7 e NS8
- **Test di Rete**: Verificate la connettività prima di avviare la migrazione:
  ```bash
  # Da NS7, testate la connettività della porta VPN
  nc -zv <ns8-leader-fqdn> 55820
  ```

### Requisiti DNS

Una corretta configurazione DNS è critica per la migrazione di NethVoice:

- **Accesso al Server DNS**: Dovete avere accesso amministrativo al vostro server DNS autoritativo
- **Gestione Record DNS**: Capacità di creare e modificare record DNS

#### FQDN Richiesti per NethVoice

Dovete pianificare e preparare **due FQDN separati**:

| Scopo FQDN | Esempio | Descrizione |
|-----------|---------|-------------|
| **Amministrazione NethVoice** | `nethvoice.example.com` | Accesso all'interfaccia di amministrazione di NethVoice. Potete utilizzare questo FQDN anche per il proxy se avete intenzione di installare solo un'istanza di NethVoice. |
| **CTI NethVoice** | `cti.example.com` | Accesso all'applicazione web NethVoice CTI |

:::warning Pianificazione FQDN
Pianificate questi FQDN con attenzione prima di avviare la migrazione. Dovrete fornirli durante il processo di migrazione e i record DNS devono essere aggiornati dopo il completamento della migrazione.
:::

Se state consolidando più istanze di NethVoice dietro un singolo proxy, dovrete anche pianificare un FQDN aggiuntivo per il proxy stesso, come `proxy.example.com`.

#### Tipi di Record DNS

Dovrete creare o aggiornare:
- **Record A**: Puntamento all'indirizzo IP del nodo NS8
- **Record CNAME** (opzionale): Se si utilizzano alias

#### Propagazione DNS

- Consentite 24-48 ore per la propagazione DNS dopo l'aggiornamento dei record
- Considerate l'utilizzo di valori TTL bassi prima della migrazione per accelerare la propagazione
- Testate la risoluzione DNS da più posizioni dopo l'aggiornamento

## Prerequisiti del Provider di Account

La configurazione del provider di account dipende dalla vostra configurazione NS7 attuale.

### Provider di Account Locale (OpenLDAP o Samba AD)

Se NS7 utilizza un provider di account locale:

#### OpenLDAP
- **Nome Dominio**: Scegliete un nome di dominio univoco per il cluster NS8
- **Rinomina Consentita**: Il dominio può essere rinominato durante il processo di connessione
- **Nessun Conflitto**: Assicuratevi che il nome scelto non entri in conflitto con i domini NS8 esistenti

#### Active Directory (Samba)
- **Nome Dominio Fisso**: I nomi di dominio AD non possono essere modificati durante la migrazione
- **Pre-controllo Richiesto**: Verificate che il vostro nome di dominio AD non entri in conflitto con i domini NS8 esistenti
- **Nome Univoco**: Il nome del dominio deve essere univoco all'interno del cluster NS8

:::info Dominio Esterno Temporaneo
Durante la migrazione, viene creato un dominio utente esterno temporaneo in NS8 per consentire alle applicazioni migrate di accedere al provider di account NS7. Questo viene rimosso automaticamente una volta completata la migrazione del provider di account.
:::

### Provider di Account Remoto

Se NS7 utilizza un provider di account remoto (LDAP/AD esterno):

1. **Configurazione Corrispondente Richiesta**: NS8 deve avere un dominio utente esterno configurato che corrisponda alla vostra configurazione NS7
2. **Corrispondenza BaseDN**: Il dominio esterno NS8 deve corrispondere al BaseDN di NS7
   
   **Esempio**:
   - NS7 BaseDN: `dc=directory,dc=nh`
   - Il nome di dominio NS8 deve essere: `directory.nh`

3. **Stesso Database LDAP**: Il dominio utente esterno NS8 deve puntare allo stesso database LDAP di NS7
4. **Accesso a Livello di Cluster**: Tutti i nodi nel cluster NS8 devono essere in grado di raggiungere il database LDAP
5. **Accessibilità Futura**: Assicuratevi che il database LDAP rimanga accessibile dopo la disattivazione di NS7

:::warning Configurazione Provider Esterno
Configurate il dominio utente esterno in NS8 **prima** di avviare la migrazione. Fare riferimento alla guida [Configurazione Provider di Account](https://docs.nethserver.org/projects/ns8/en/latest/user_domains.html).
:::

## Preparazione Dati

### Strategia di Backup

**Create un backup completo prima della migrazione**:

Utilizzate il modulo di backup NS7 o la vostra soluzione di backup preferita per eseguire un backup completo del sistema.

:::warning Backup è Obbligatorio
Non procedete mai con la migrazione senza un backup completo e verificato. Testate la procedura di ripristino del backup prima di iniziare.
:::

### Pianificazione Risorse

Stimate le risorse necessarie per la migrazione:

#### Calcolo Spazio Disco

Calcolate lo spazio disco richiesto su NS8:

| Tipo di Dati | Posizione su NS7 | Dimensione Tipica |
|-----------|-----------------|--------------|
| **Registrazioni Chiamate** | `/var/spool/asterisk/monitor/` | Varia (può essere 10GB - 500GB+) |
| **File Audio** | `/var/lib/asterisk/sounds/custom/` | 100MB - 1GB |
| **Database CDR** | Database MySQL | 500MB - 10GB+ |
| **Segreteria Telefonica** | `/var/spool/asterisk/voicemail/` | 1GB - 20GB+ |
| **Configurazione** | Varia | < 100MB |

Controllate l'utilizzo effettivo:
```bash
# Su NS7, controllate la dimensione della registrazione
du -sh /var/spool/asterisk/monitor/

# Controllate la dimensione della segreteria
du -sh /var/spool/asterisk/voicemail/

# Controllate la dimensione del database CDR
mysql -e "SELECT table_schema AS 'Database', 
ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)' 
FROM information_schema.TABLES 
WHERE table_schema = 'asteriskcdrdb' 
GROUP BY table_schema;"
```

#### Pianificazione Rete e Ora

- **Larghezza di Banda di Rete**: Una larghezza di banda più elevata riduce il tempo di sincronizzazione
- **Sincronizzazione Iniziale**: Può richiedere diverse ore a seconda del volume di dati
- **Sincronizzazioni Incrementali**: Le sincronizzazioni successive sono più veloci (solo modifiche)
- **Cutover Finale**: Pianificate 30 minuti a 2 ore di inattività per la migrazione finale

:::tip Ridurre il Downtime
Eseguite più sincronizzazioni di dati prima del cutover finale. Questo riduce al minimo la finestra di inattività finale poiché è necessario trasferire solo i dati modificati.
:::

## Lista di Controllo Pianificazione Pre-Migrazione

Completate questa lista di controllo prima di avviare la migrazione:

### Preparazione di Sistema
- [ ] Sistema NS7 accessibile tramite SSH e Cockpit
- [ ] NS7 completamente aggiornato all'ultima versione
- [ ] NS7 NethVoice in esecuzione senza errori
- [ ] Cluster NS8 installato e operativo
- [ ] Cluster NS8 accessibile tramite interfaccia web
- [ ] Proxy NethVoice installato sul nodo di destinazione (consigliato)

### Preparazione di Rete
- [ ] Connettività di rete verificata tra NS7 e NS8
- [ ] Porta VPN 55820 accessibile da NS7 a NS8
- [ ] FQDN del nodo leader NS8 risolto correttamente da NS7
- [ ] Regole firewall riviste e regolate se necessario

### Preparazione DNS
- [ ] Accesso amministrativo al server DNS confermato
- [ ] Due FQDN scelti per NethVoice e CTI
- [ ] Procedura di aggiornamento DNS documentata
- [ ] Valori TTL ridotti (opzionale, per propagazione più veloce)

### Preparazione Provider di Account
- [ ] Tipo di provider di account identificato (locale/remoto, OpenLDAP/AD)
- [ ] Conflitti di nomi di dominio controllati
- [ ] Per provider remoto: Dominio esterno configurato in NS8
- [ ] Univocità del nome di dominio verificata

### Preparazione Dati
- [ ] Backup completo del sistema NS7 creato
- [ ] Verifica del backup completata
- [ ] Requisiti di spazio disco calcolati
- [ ] NS8 ha spazio disco disponibile sufficiente
- [ ] Stime del volume di dati documentate

### Pianificazione e Comunicazione
- [ ] Finestra di inattività programmata
- [ ] Utenti notificati della migrazione imminente
- [ ] Team di supporto informato sulla pianificazione della migrazione
- [ ] Piano di rollback documentato
- [ ] Elenco di contatti di emergenza preparato

### Documentazione
- [ ] Configurazione attuale documentata
- [ ] Elenco di interni esportato
- [ ] Credenziali trunk registrate (in modo sicuro)
- [ ] Configurazioni personalizzate annotate
- [ ] Diagramma di rete aggiornato

## Risorse Aggiuntive

Prima di procedere, consultate queste risorse:

- **[Guida all'Installazione NethServer 8](../../administrator-manual/install/nethserver.md)** - Setup completo NS8
- **[Installazione Proxy NethVoice](../../administrator-manual/advanced/nethvoice_proxy.md)** - Setup e configurazione del proxy
- **[Guida Ufficiale Migrazione NS8](https://docs.nethserver.org/projects/ns8/en/latest/migration.html)** - Procedure di migrazione generale NS8
- **[Configurazione Provider di Account](https://docs.nethserver.org/projects/ns8/en/latest/user_domains.html)** - Setup dominio utente in NS8

## Passaggi Successivi

Una volta che tutti i prerequisiti sono soddisfatti e la lista di controllo è completa, procedete a:

➡️ **[Avviare la Migrazione](./start_migration)** - Iniziate il processo di migrazione

:::info Domande o Problemi?
Se incontrate problemi durante la preparazione, consultate i [forum della comunità NethServer](https://community.nethserver.org/) o contattate il supporto Nethesis prima di procedere.
:::

