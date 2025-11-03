---
title: URL parametrizzati
sidebar_position: 3
---

Consente all'utente finale di invocare un URL parametrizzato alla ricezione di una chiamata. L'URL sarà parametrizzato con i dati del chiamante e può essere "aperto" in uno dei seguenti quattro scenari:

- Mai
- Quando la chiamata in arrivo sta squillando
- Quando la chiamata in arrivo è stata risolta
- Facendo clic sul pulsante appropriato nella casella di gestione delle chiamate

Per creare un URL sono necessarie due informazioni:

- L'URL stesso
- La selezione di un profilo utente

La composizione dell'URL può essere eseguita utilizzando questi parametri, che vengono compilati per ogni chiamata:

- *\$CALLER_NUMBER* (Numero del chiamante)
- *\$CALLER_NAME* (Nome associato da NethVoice al numero del chiamante)
- *\$CALLED* (Numero chiamato)
- *\$UNIQUEID* (Identificatore univoco della chiamata)

È possibile abilitare l'opzione "Solo chiamate alle code" per attivare l'URL parametrizzato solo per le chiamate che squillano in una coda.

Tutti gli utenti che dispongono di quel profilo potranno utilizzare l'URL appena creato.

:::note
- Solo un URL può essere associato a un profilo.
- Affinché l'URL venga richiamato, è necessario che l'utente finale abbia abilitato la visualizzazione dei popup nel suo browser!
:::
