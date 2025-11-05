# Scripts

This directory contains utility scripts for managing the NethVoice documentation.

## Import Scripts

### Import a RST Document

Enter this directory:
```
cd scripts
```

then run:
```
./import.sh https://raw.githubusercontent.com/NethServer/ns8-docs/refs/heads/main/nethvoice_proxy.rst
```

### Import a Freshdesk FAQ

```bash
FRESHDESK_API_TOKEN=xxx ./import-freshdesk-faq.sh https://helpdesk.nethesis.it/a/solutions/articles/3000128249
```

````
