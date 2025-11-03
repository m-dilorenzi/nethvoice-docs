---
title: Provisioning gateway
sidebar_position: 4
---

# Provisioning gateway

## Gateway Supportati

Vedere [gateway supportati](supported_gateways) per un elenco di gateway supportati e le loro versioni firmware.

## Provisioning

La configurazione del gateway viene eseguita utilizzando la Procedura guidata.

Il provisioning segue le stesse regole generali del provisioning dei telefoni, con una differenza importante: NethVoice carica la configurazione sul gateway tramite una connessione telnet diretta, quindi il gateway non deve recuperare la sua configurazione.

I gateway devono essere online per ricevere un caricamento automatico; per impostazione predefinita si avviano in modalità `DHCP`. Tuttavia, è anche possibile preparare un file di configurazione in anticipo per un gateway non ancora connesso utilizzando **Aggiungi Gateway**. Il file generato può quindi essere caricato manualmente tramite l'interfaccia web del gateway quando il dispositivo è disponibile.

### Configurazione dei Gateway

Per configurare il gateway, è necessario specificare alcuni parametri di configurazione richiesti:

1. **IP Dispositivo**: Inserire l'indirizzo IP da assegnare al gateway, assicurandosi che sia nella stessa subnet del sistema NethVoice, ad es. `192.168.1.100`
2. **Indirizzo MAC**: Inserire l'indirizzo MAC del dispositivo gateway, solitamente indicato su un'etichetta sul dispositivo stesso, ad es. `00:11:22:AA:BB:CC`
3. **Subnet mask**: Specificare la subnet mask per il gateway, solitamente qualcosa come `255.255.255.0`
4. **Gateway di rete**: Inserire l'indirizzo IP del gateway, tipicamente l'indirizzo IP del router sulla rete locale. Ad es. `192.168.1.1`
5. **IP PBX**: Inserire l'FQDN (consigliato) o l'indirizzo IP del sistema NethVoice a cui il gateway si connetterà.
6. Inserire tutte le caratteristiche richieste per la configurazione delle linee collegate (per linee ISDN, la modalità dell'adattatore terminale ISDN; per linee analogiche, il numero composto della linea).
   
   Queste impostazioni dipendono dal modello:

    - `ISDN` (Specificare se la linea è Point-to-Point o Point-to-Multipoint)
    - `PRI`
    - `FXS` (Specificare per ogni porta l'interno da assegnare scegliendo un utente precedentemente configurato)
    - `FXO` (Specificare il numero direttamente nel campo di testo)


:::note
Per i modelli Grandstream con 2 interfacce di rete, deve essere fornito l'indirizzo MAC dell'interfaccia LAN, ma la configurazione di NethVoice utilizza l'interfaccia WAN, che sarà quella utilizzata.
:::

Per scaricare la configurazione del gateway per il caricamento tramite l'interfaccia web, fare clic sul pulsante di gestione (simbolo con tre quadrati).

