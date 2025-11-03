---
title: Click to Call
sidebar_position: 10
---

# Click to Call

## Panoramica

**Click-to-Call** è una potente funzionalità che consente agli utenti di avviare chiamate telefoniche semplicemente facendo clic su un numero di telefono visualizzato in applicazioni, pagine web o fonti di dati clienti. Questo elimina la necessità di comporre manualmente i numeri e razionalizza il processo di avvio delle chiamate.

Quando un utente fa clic su un numero di telefono, NethVoice identifica automaticamente il dispositivo e instrada la chiamata attraverso il sistema telefonico appropriato:

- **Utenti Web Phone** → Chiamata diretta tramite interfaccia NethVoice CTI
- **Utenti Desktop** → Chiamata tramite applicazione desktop NethLink
- **Utenti Telefono fisico** → Chiamata indirizzata al telefono da scrivania configurato

:::info Vantaggio chiave
Click-to-Call migliora notevolmente l'efficienza degli utenti riducendo i passaggi necessari per effettuare una chiamata. Invece di copiare un numero e comporlo manualmente, gli utenti semplicemente cliccano e si connettono.
:::

## Scenari supportati

Click-to-Call funziona in tre diverse configurazioni a seconda del dispositivo telefonico dell'utente:

| Scenario | Tipo di dispositivo | Configurazione richiesta | Ideale per |
|----------|-------------|-----------------|----------|
| **Web Phone** | Basato su browser | Solo NethVoice CTI | Lavoratori remoti, posizioni flessibili |
| **Client Desktop** | NethLink + Telefono fisico | NethLink + Telefono | Lavoratori d'ufficio con telefoni da scrivania |
| **Telefono fisico** | Telefono SIP provisioning | NethLink + Phone provisioning | Implementazioni standard d'ufficio |

---

## 1. Web Phone (NethVoice CTI)

### Di cosa si tratta

Web Phone è un client telefonico basato su software integrato direttamente nell'interfaccia web **NethVoice CTI**. Funziona interamente nel browser web e non richiede alcuna installazione di software aggiuntivo.

### Come funziona

Quando fai clic su un numero di telefono in NethVoice CTI:
1. Il sistema rileva l'evento clic
2. NethVoice lo interpreta come un'iniziazione di chiamata
3. La chiamata viene instradata attraverso NethVoice al sistema telefonico
4. Rispondi alla chiamata direttamente nel browser

### Requisiti di configurazione

✅ **Già incluso** - Nessuna configurazione aggiuntiva necessaria!

Click-to-Call è automaticamente disponibile per tutti gli utenti NethVoice CTI all'interno dell'interfaccia web.

### Dove fare clic

I numeri di telefono possono essere cliccati in:
- **Rubrica contatti** (rubrica indirizzi)
- **Cronologia chiamate** (chiamate recenti)
- **Schede clienti** (dati CRM)
- **Directory aziendale** (elenco utenti)
- **Qualsiasi numero di telefono visualizzato** in NethVoice CTI

### Vantaggi

- ✅ Nessuna installazione di software aggiuntivo
- ✅ Funziona su qualsiasi dispositivo con browser web
- ✅ Chiama direttamente dal browser
- ✅ Compatibile con dispositivi mobili
- ✅ Accessibile da qualsiasi luogo

### Limitazioni

- Le chiamate sono limitate al solo client Web Phone
- Non è possibile trasferire le chiamate a telefoni fisici
- Possono esserci limitazioni se l'audio/microfono non è disponibile

---

## 2. Client Desktop (NethLink)

### Di cosa si tratta

**NethLink** è un'applicazione desktop per Windows e Mac che estende la funzionalità Click-to-Call all'intero sistema operativo. Una volta installata e configurata, facendo clic sui numeri di telefono ovunque sul desktop (email, browser web, documenti, ecc.) verranno automaticamente avviate le chiamate attraverso il telefono configurato.

### Come funziona

Quando fai clic su un numero di telefono sul computer:
1. NethLink rileva il clic su un collegamento di protocollo `tel:` o `callto:`
2. NethLink cattura il numero di telefono
3. NethLink instrada la chiamata al dispositivo configurato
4. Il telefono squilla e puoi rispondere

### Prerequisiti

Prima di utilizzare Click-to-Call con NethLink, è necessario:

1. **Installare NethLink** sul computer Windows o Mac
2. **Configurare NethLink** con le credenziali NethVoice
3. **Fare in modo che un amministratore abiliti NethLink** per il tuo account utente in NethVoice
4. **Selezionare un dispositivo telefono principale** (Web Phone, telefono desktop o telefono fisico)

### Istruzioni di configurazione

#### Passaggio 1: Installare NethLink

- Scarica NethLink per [Windows](https://nethserver.github.io/nethlink/) o [Mac](https://nethserver.github.io/nethlink/)
- Installa l'applicazione seguendo le procedure di installazione standard
- Avvia NethLink all'avvio

#### Passaggio 2: Abilita per il tuo utente (Compito amministratore)

Un amministratore NethVoice deve abilitare NethLink per il tuo account utente:

1. Apri **Amministrazione NethVoice**
2. Vai a **Configurazione** → **Utenti**
3. Seleziona il tuo account utente
4. Abilita il dispositivo **"Phone Link"**
5. Salva le modifiche

#### Passaggio 3: Configura NethLink

Apri NethLink sul desktop e:

1. Inserisci le **credenziali di accesso CTI NethVoice**
2. Specifica l'**indirizzo del server NethVoice** (FQDN o IP)
3. Seleziona il **dispositivo principale** per le chiamate
4. Testa la connessione

Consulta la [Documentazione NethLink](https://nethserver.github.io/nethlink/) per i passaggi di configurazione dettagliati.

#### Passaggio 4: Imposta come gestore di protocollo predefinito

Configura il sistema operativo per utilizzare NethLink per i clic sui numeri di telefono:

**Windows:**
1. Fai clic destro su un collegamento `tel:` nel browser
2. Seleziona "Apri con" → "Scegli un'altra applicazione"
3. Seleziona **NethLink** e seleziona "Usa sempre questa app"

**Mac:**
1. Apri **Preferenze Sistema** → **Generali**
2. Trova l'impostazione "Browser web predefinito"
3. Configura i gestori di protocollo attraverso le impostazioni di Safari o Chrome

### Dove fare clic

Una volta configurato, puoi fare clic sui numeri di telefono in:
- **Client email** (Outlook, Gmail, Thunderbird)
- **Browser web** (qualsiasi collegamento `tel:`)
- **Documenti** (Word, PDF, Google Docs)
- **Gestori di contatti** (Contatti Outlook, Google Contatti)
- **Qualsiasi applicazione** che supporti i collegamenti ai numeri di telefono

### Vantaggi

- ✅ Funziona a livello di sistema in tutte le applicazioni
- ✅ Composizione con un clic da qualsiasi luogo del desktop
- ✅ Integrazione fluida con le applicazioni familiari
- ✅ Chiama al telefono desktop o a qualsiasi dispositivo configurato
- ✅ Aumento dell'efficienza professionale

### Limitazioni

- Richiede l'installazione di NethLink
- Richiede la configurazione dell'amministratore
- Il telefono desktop deve essere sulla stessa rete o accessibile tramite VPN

---

## 3. Telefono fisico (Telefono da scrivania)

### Di cosa si tratta

Per gli utenti con **telefoni fisici provisioning** (telefoni da scrivania configurati tramite NethVoice provisioning), Click-to-Call funziona tramite **NethLink** per inviare la chiamata al telefono fisico.

### Come funziona

Quando fai clic su un numero di telefono:
1. NethLink rileva il protocollo `tel:`
2. NethLink invia l'iniziazione della chiamata a NethVoice
3. NethVoice instrada la chiamata al tuo **telefono fisico**
4. Il telefono da scrivania squilla
5. Rispondi alla chiamata sul telefono fisico

### Prerequisiti

Per Click-to-Call con telefono fisico, è necessario:

1. **Accesso CTI NethVoice** con account utente attivo
2. **Telefono fisico provisioning** in NethVoice (registrato con indirizzo MAC)
3. **Telefono fisico assegnato al tuo utente** in NethVoice
4. **NethLink installato e configurato** sul desktop
5. **Telefono fisico sulla stessa rete** O **accessibile tramite VPN**
6. **Connettività di rete** tra il computer e il telefono

### Requisiti di rete

Il requisito più importante è la **connettività di rete tra il computer e il telefono fisico**:

- ✅ **Stessa LAN** - Connessione di rete diretta
- ✅ **VPN connessa** - Ufficio remoto connesso tramite VPN
- ✅ **Percorso IP diretto** - Reti con routing configurato
- ❌ **Solo Internet** - Telefono su Internet, computer su rete diversa (NON funzionerà)

:::warning Dipendenza di rete
Click-to-Call ai telefoni fisici richiede comunicazione diretta sulla rete. Se lavori da remoto e il telefono è in ufficio senza accesso VPN, questo scenario non funzionerà.
:::

### Istruzioni di configurazione

#### Passaggio 1: Assicurati che il telefono sia provisioning

1. In **Amministrazione NethVoice**, vai a **Dispositivi** → **Telefoni**
2. Verifica che l'**indirizzo MAC del telefono sia registrato**
3. Verifica che il **modello del telefono sia selezionato correttamente**

#### Passaggio 2: Associa il telefono al tuo utente

1. Vai a **Configurazione** → **Utenti**
2. Seleziona il tuo account utente
3. In **Dispositivi associati**, assegna il tuo **telefono fisico**
4. Assicurati che il telefono sia impostato come dispositivo
5. Salva le modifiche

#### Passaggio 3: Installa e configura NethLink

Segui le istruzioni di configurazione del client desktop precedenti per:
- Installare NethLink
- Configurare con le tue credenziali
- Selezionare il telefono fisico come dispositivo principale

#### Passaggio 4: Test Click-to-Call

1. Apri NethVoice CTI
2. Trova un numero di telefono (in rubrica o cronologia chiamate)
3. Fai clic sul numero di telefono
4. Verifica che il telefono fisico squilli
5. Rispondi alla chiamata

### Vantaggi

- ✅ Esperienza professionale con telefono da scrivania
- ✅ Telefono fisico familiare per le chiamate
- ✅ Supporta tutte le funzioni telefoniche (trasferimento, attesa, ecc.)
- ✅ Click-to-Call a livello di sistema sul desktop

### Limitazioni

- Richiede telefono provisioning in NethVoice
- Richiede connettività di rete al telefono
- Non adatto per lavoratori completamente remoti (telefono in ufficio)
- Richiede installazione NethLink

---

## Risoluzione dei problemi

### Web Phone Click-to-Call non funziona

**Problema:** Fare clic sui numeri in NethVoice CTI non avvia le chiamate

**Soluzioni:**
- Verifica di essere **connesso a NethVoice CTI**
- Controlla che il browser **consenta l'accesso al microfono**
- Assicurati che il **dispositivo Web Phone sia abilitato** per il tuo utente
- Svuota la cache del browser e ricarica CTI
- Prova un browser diverso

### NethLink non intercetta i clic su telefono

**Problema:** Fare clic sui collegamenti `tel:` non avvia NethLink

**Soluzioni:**
- Verifica che **NethLink sia in esecuzione** (controlla nel vassoio di sistema)
- Reinstalla NethLink per registrare il gestore di protocollo
- Imposta manualmente NethLink come predefinito per il protocollo `tel:`
- Verifica che **NethLink sia abilitato** per il tuo utente in NethVoice
- Verifica che **NethLink possa connettersi** al server NethVoice (test della connessione)

### Telefono fisico non squilla

**Problema:** Click-to-Call invia la chiamata ma il telefono non squilla

**Soluzioni:**
- Verifica che il **telefono sia registrato** in NethVoice
- Verifica che il **telefono sia assegnato al tuo account utente**
- Verifica la **connettività di rete** tra il computer e il telefono
- Verifica che il **telefono sia acceso** e abbia una connessione di rete
- Testa manualmente il telefono per confermarne il funzionamento
- Verifica che **telefono e computer si possono pingare** a vicenda
- Controlla le regole del firewall (se applicabile)

### Nessun audio dopo la connessione della chiamata

**Problema:** La chiamata si connette ma non viene udito alcun audio

**Soluzioni:**
- Controlla le **impostazioni del microfono del browser** (per Web Phone)
- Verifica che il **dispositivo audio sia selezionato** nelle impostazioni di sistema
- Testa il microfono nelle impostazioni di sistema
- Verifica i permessi del browser per l'accesso al microfono
- Prova a disabilitare la cancellazione del rumore di fondo
- Riavvia NethLink o il browser

---

## Best practice

### Per gli amministratori

- ✅ Abilita NethLink per gli utenti che ne hanno bisogno
- ✅ Assicurati che i telefoni siano correttamente provisioning
- ✅ Verifica la connettività di rete per i lavoratori remoti
- ✅ Testa la funzionalità Click-to-Call dopo la configurazione
- ✅ Documenta le procedure di configurazione per gli utenti

### Per gli utenti

- ✅ Usa Web Phone per semplici chiamate basate su browser
- ✅ Installa NethLink se hai bisogno di Click-to-Call a livello di sistema
- ✅ Mantieni NethLink in esecuzione per l'intercettazione automatica
- ✅ Segnala i problemi di rete se il telefono non squilla
- ✅ Testa la funzionalità nel tuo ambiente

---

## Riepilogo

| Metodo | Configurazione | Ideale per | Limitazioni |
|--------|-------|----------|-------------|
| **Web Phone** | Integrato | Composizione basata su browser, lavoratori remoti | Solo interfaccia CTI |
| **NethLink** | Semplice | Click-to-Call su desktop ovunque | Richiede installazione |
| **Telefono fisico** | Moderata | Implementazioni d'ufficio professionali | Dipende dalla rete |

Scegli il metodo che meglio si adatta alle esigenze della tua organizzazione e al modello di implementazione.
