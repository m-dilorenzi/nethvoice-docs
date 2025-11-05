---
title: Gestione massiva
sidebar_position: 5
---

# Gestione massiva

La sezione *Gestione massiva* consente di gestire e modificare simultaneamente più interni e telefoni, migliorando l'efficienza operativa quando si effettuano modifiche a gruppi di utenti o dispositivi.

## Gestione Massiva Interni {#bulk-extensions-users}

La funzione *Gestione massiva interni/utenti* consente di modificare più interni utente e le loro impostazioni in una singola operazione.

### Selezione degli Interni

Per modificare più interni:

1. Utilizzare il menu a discesa **Seleziona** per scegliere gruppi specifici di interni
2. In alternativa, spuntare le caselle di controllo accanto ai singoli interni nell'elenco
3. È possibile selezionare più interni utilizzando una combinazione di entrambi i metodi

### Modifica degli Interni

Una volta selezionati gli interni da modificare:

1. Fare clic sul bottone **Modifica**
2. Verrà visualizzata una finestra di configurazione che mostra le impostazioni disponibili
3. I campi visualizzeranno i valori solo se tutti gli interni selezionati hanno lo stesso valore per quel campo
4. Se gli interni selezionati hanno valori diversi per un campo, il campo rimarrà vuoto

### Stato del Blocco del Campo {#field-lock-status}

Ogni campo ha un'icona di lucchetto sul lato destro:

- **Lucchetto Chiuso**: Il campo non verrà modificato al momento del salvataggio
- **Lucchetto Aperto**: Il valore del campo verrà sovrascritto con il nuovo valore al momento del salvataggio

### Esempio

Ad esempio, se gli interni 201 e 202 hanno valori di gruppo di chiamata diversi:

- Il campo del gruppo di chiamata apparirà vuoto
- Con il lucchetto chiuso, i valori esistenti rimarranno invariati al salvataggio
- Se si apre il lucchetto e si salva, il valore del gruppo di chiamata verrà sovrascritto per entrambi gli interni

## Gestione Massiva Telefoni {#bulk-phones}

La funzione *Gestione massiva telefoni* consente di gestire e configurare più telefoni simultaneamente in base a gruppi di utenti o modelli di telefoni.

### Selezione dei Telefoni

Da **Applicazioni > Gestione multipla telefoni**, è possibile:

1. Selezionare più telefoni utilizzando criteri di gruppo (gruppi di utenti)
2. Filtrare per modello di telefono
3. Una volta applicati uno o più criteri di selezione, è possibile eseguire azioni in base alla selezione

### Riavvio {#restart}

Le impostazioni di provisioning vengono applicate automaticamente ai telefoni ogni notte se gli aggiornamenti automatici sono abilitati. Se gli aggiornamenti automatici non sono abilitati, è necessario riavviare manualmente i telefoni utilizzando questa funzione.

**Importante**: Solo i telefoni che hanno completato la registrazione SIP possono essere riavviati da questa pagina.

È possibile riavviare i telefoni immediatamente o pianificare il riavvio per un'ora futura:

- **Riavvia ora**: Riavvia immediatamente i telefoni selezionati
- **Riavvio ritardato**: Pianifica il riavvio per un'ora specifica nel futuro

### Assegna Modello {#assign-model}

Se i telefoni selezionati provengono dallo stesso produttore, è possibile assegnare lo stesso modello a tutti loro utilizzando il bottone **Assegna modello**. Questo è utile quando si standardizzano le configurazioni dei telefoni in un gruppo di utenti.
