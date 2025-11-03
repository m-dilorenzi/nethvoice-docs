---
title: Bypass proxy per trunk senza registrazione
sidebar_position: 1
tags: 
  - proxy
  - trunk
---

Questa procedura è necessaria solo se un trunk VoIP non registrato (ad esempio, un trunk basato su IP senza credenziali di registrazione SIP) non funziona correttamente quando instradato attraverso l'istanza NethVoice Proxy.

L'obiettivo è instradare le chiamate con una radice specifica (prefisso) direttamente a un'istanza NethVoice (il PBX interno) **senza farle passare attraverso il motore SIP/RTP di NethVoice Proxy (Kamalio/RTP Engine).**

### 1. Prerequisiti

* Il modulo **NethVoice Proxy** deve essere installato e configurato.
* Almeno un'istanza **NethVoice** (ad esempio, `nethvoice1`) deve essere installata e configurata.
* Il trunk VoIP deve essere configurato all'interno dell'istanza NethVoice di destinazione (ad esempio, `nethvoice1`) come **Trunk Peer/Host** o simile, e deve essere di tipo "non registrato".

### 2. Accesso alle regole di instradamento dei trunk

1. Accedi all'interfaccia di amministrazione di NethServer 8.
2. Nel pannello di navigazione sinistro, seleziona la tua istanza **NethVoice Proxy** (nell'esempio: `nethvoice-proxy1`).
3. Accedi alla sezione **Regole di instradamento trunk**.
   * *Nota: Se vedi "Nessuna applicazione NethVoice disponibile", devi prima installare e configurare almeno un'istanza NethVoice.*

### 3. Creazione della regola di bypass

Questa regola indica a NethVoice Proxy di bypassare la sua gestione per un prefisso specifico e instradare il traffico direttamente all'istanza NethVoice scelta.

1. Fai clic sul pulsante **Aggiungi regola**.
2. Apparirà la finestra di dialogo **Aggiungi regola**.
3. Configura la regola:
   * **Radice:** Immetti un **prefisso univoco** che agirà come trigger per questa regola di bypass.
      * **Importante:** Scegli una stringa numerica **non parte** dello schema di numerazione interno o dei prefissi esterni standard (ad esempio, `456`, come mostrato nell'esempio). Questo prefisso verrà intercettato dal proxy e instradato.
   * **Applicazione di destinazione:** Seleziona l'istanza NethVoice che contiene il trunk VoIP che desideri bypassare (ad esempio, `nethvoice1 [10.5.4.1]`).
4. Fai clic su **Salva**.

### 4. Verifica e configurazione del PBX

1. Una volta salvata, la regola apparirà nell'elenco **Regole di instradamento trunk** e verrà visualizzata una notifica "Completato".
2. Il passaggio finale e cruciale è configurare il PBX dell'istanza NethVoice per gestire le chiamate utilizzando questo prefisso di bypass:

   * **Per chiamate in uscita:** Configura una **Rotta in uscita** nel tuo PBX NethVoice. Il modello di composizione dovrebbe includere il prefisso **Radice** configurato (ad esempio, `456`). Questa rotta dovrebbe essere indirizzata al trunk non registrato specifico.
      * Il PBX dovrebbe quindi eliminare il prefisso `456` prima di inviare il numero al trunk/provider.
   * **Per chiamate in arrivo (dal trunk non registrato):** Il provider/gateway che invia la chiamata a NethVoice Proxy deve anteporre il prefisso **Radice** configurato (`456`) al numero di destinazione (DID). Il PBX, al ricevimento della chiamata sul trunk non registrato, può quindi utilizzare una **Rotta in arrivo** corrispondente a quel prefisso per indirizzare la chiamata internamente.

### Come funziona il bypass

Quando una chiamata (in uscita dal PBX o in arrivo da un gateway/provider) viene elaborata da NethVoice Proxy, il proxy verifica la parte iniziale della stringa di composizione (la **Radice**).

Se la chiamata corrisponde al prefisso configurato (ad esempio, `456`), il proxy instrada la chiamata **direttamente** al sistema PBX NethVoice specificato (`nethvoice1`), bypassando la sua gestione interna di SIP e RTP (Kamalio/RTP Engine). Ciò garantisce che il traffico VoIP dal trunk/gateway non registrato specifico, che potrebbe avere problemi di compatibilità con il proxy, sia gestito direttamente dal PBX.
