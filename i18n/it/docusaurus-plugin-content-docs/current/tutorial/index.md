title: Getting started
sidebar_position: 1


# Guida introduttiva a NethVoice

NethVoice è una piattaforma di telefonia e comunicazione unificata che offre funzionalità PBX per piccole e medie imprese.
Fornisce instradamento delle chiamate, segreteria telefonica, conferenze e gestione utenti tramite un'interfaccia web intuitiva.
Progettata per funzionare su [NethServer](https://www.nethserver.org/), NethVoice supporta installazioni scalabili e accesso remoto sicuro tramite il Proxy NethVoice.

Questa guida ti accompagnerà nei passaggi fondamentali per configurare NethVoice sul tuo sistema.

## 1. Installare NethServer 8 {#1-install-nethserver-8}

Inizia installando NethServer 8 sul tuo server.
- Scarica e segui le istruzioni di installazione dalla [guida ufficiale](https://docs.nethserver.org/projects/ns8/it/latest/install.html).
- Dopo l'installazione, accedi all'interfaccia web su `https://<server_ip_o_fqdn>/cluster-admin/` utilizzando:
	- **Username:** `admin`
	- **Password:** `Nethesis,1234`
- Crea un cluster e assicurati che il server abbia un IP statico e un FQDN valido.

## 2. Installare e configurare il Proxy NethVoice {#2-install-and-configure-nethvoice-proxy}

Il Proxy NethVoice è necessario per abilitare l'accesso remoto sicuro ai servizi NethVoice.
- Installa il modulo Proxy NethVoice dal Software Center.
- Assegna un FQDN valido (es. `proxy.tuodominio.org`) e verifica che il record DNS sia configurato.
- Configura l'interfaccia di rete e l'IP pubblico secondo necessità.
- Può essere installato un solo Proxy NethVoice per nodo.
- Per i passaggi dettagliati, consulta la [documentazione del Proxy NethVoice](https://docs.nethvoice.com/i18n/it/docusaurus-plugin-content-docs/current/administrator-manual/install/nethvoice_install.md#step-1-install-nethvoice-proxy).

## 3. Installare il modulo NethVoice {#3-install-nethvoice-module}

Una volta configurato il proxy, puoi installare il modulo NethVoice:
- Apri il **Software Center** dall'interfaccia web.
- Cerca l'applicazione NethVoice e clicca su **Installa**.
- Per maggiori informazioni, consulta la [documentazione del Software Center](https://docs.nethserver.org/projects/ns8/it/latest/software_center.html).

## 4. Configurare NethVoice {#4-configure-nethvoice}

Dopo l'installazione, configura la tua istanza NethVoice:
- Segui la [guida alla configurazione di NethVoice](https://docs.nethvoice.com/i18n/it/docusaurus-plugin-content-docs/current/administrator-manual/install/nethvoice_install.md#module-configuration) per istruzioni dettagliate.
- Completa la configurazione iniziale, aggiungi utenti e configura l'ambiente telefonico secondo le tue esigenze.

---

Per ogni passaggio, consulta la documentazione collegata per istruzioni dettagliate e complete.

## Tutorial correlati {#tutorial-correlati}

* [Cloud vs On-Premise deployments](./cloud_vs_onpremise.md)
* [Esportare la rubrica come CSV da NethVoice](./export-phonebook-csv.md)