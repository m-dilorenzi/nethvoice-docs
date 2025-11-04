---
title: Configurazione e gestione di NethHotel
sidebar_position: 1
---

# NethHotel

NethHotel è un modulo specializzato di NethVoice progettato per la gestione degli interni configurati correttamente come camere di hotel. Fornisce funzionalità complete per gestire le comunicazioni degli ospiti, la fatturazione e l'integrazione del sistema di gestione della proprietà.

Per impostazione predefinita, l'accesso a NethHotel è concesso all'utente admin.

## Configurazione

### Abilitazione di NethHotel

NethHotel può essere abilitato nella configurazione dell'istanza di NethVoice:

1. Accedi alle applicazioni di NethVoice all'interno di NethServer
2. Vai alla pagina **Impostazioni**
3. Seleziona l'opzione **Abilita modulo hotel**
4. (Facoltativo) Specifica l'indirizzo e la porta del server FIAS se utilizzi l'integrazione PMS
5. Salva le modifiche

### Configurazione del PBX

Dopo aver abilitato il modulo NethHotel, è necessaria una certa configurazione sul lato NethVoice:

1. **Crea rotte in uscita**
   - Nell'interfaccia avanzata di NethVoice, vai a **Connettività > Rotte in uscita**
   - Crea una rotta in uscita dedicata per le camere dell'hotel
   - Utilizza un prefisso (in genere `0`) e posizionalo alla fine dell'elenco delle rotte
   - Fai clic su **Salva** e **Applica configurazione**

2. **Configura profilo hotel**
   - Dalla pagina della procedura guidata di NethVoice, accedi al profilo Hotel
   - Abilita la rotta in uscita appena creata

3. **Aggiungi interni delle camere**
   - Aggiungi gli interni delle camere al profilo hotel utilizzando il pannello di configurazione di NethVoice o lo strumento di gestione di più interni
   - Tutti gli interni inclusi nel profilo hotel verranno automaticamente gestiti da NethHotel

### Accesso a NethHotel

L'applicazione NethHotel è accessibile a:
```
https://<nethvoice_domain>/freepbx/hotel/rooms.php
```

Può essere accessibile anche dalla procedura guidata dell'amministratore di NethVoice: **Amministrazione** → **Avanzate (freepbx)** → **Applicazioni** → **NethHotel**

## Come configurare il PBX

Consigliamo la seguente configurazione:

### Interni delle camere

- Tutti gli interni delle camere devono essere aggiunti al profilo hotel tramite la sezione Configurazioni o utilizzando l'applicazione Gestione di più interni

### Interni dei servizi

- Gli interni dei servizi (come la ricezione) **non** devono essere aggiunti al profilo hotel
- Configurarli come interni standard seguendo la policy di numerazione dell'hotel
- Esempio: Se gli interni delle camere vanno da 201 a 299, imposta la ricezione come 200 o 300
- Consenti alle camere di chiamare la ricezione configurando un numero di selezione rapida (vedi [Numeri di selezione rapida](#speed-dial-numbers))
- Gli interni dei servizi possono chiamarsi direttamente l'un l'altro

### Numeri a selezione rapida {#speed-dial-numbers}

I numeri a selezione rapida consentono agli ospiti nelle camere di accedere rapidamente ai servizi come la ricezione.

Configura i numeri di selezione rapida nel profilo hotel per abilitare le camere di chiamare i servizi configurati.

### Rotte in uscita

- Utilizza una rotta in uscita separata **senza** prefisso per gli interni dei servizi
- Questo dovrebbe essere diverso dalla rotta utilizzata per gli interni delle camere

## Codici funzionalità del telefono

Nell'interfaccia di gestione PBX di NethVoice, in **Codici servizio**, puoi trovare i codici da utilizzare per le funzionalità di NethHotel direttamente dai telefoni.

### Codici funzionalità di esempio

Aggiungi un addebito extra a una camera:
```
*33 + Interno della camera + # + ID extra + # + Quantità
```
