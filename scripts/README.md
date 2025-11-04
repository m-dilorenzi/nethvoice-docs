# Scripts

This directory contains utility scripts for managing the NethVoice documentation.

---

## DocIndexer

Automatically maintain and update `index.md` files across the documentation tree.

### Purpose

The `doc_indexer.py` script keeps documentation directory indices up-to-date by scanning all Markdown files in each directory and generating a "## Contents" section that lists them.

### Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run on English documentation
python doc_indexer.py ../docs

# Run on Italian documentation
python doc_indexer.py ../i18n/it/docusaurus-plugin-content-docs/current
```

### Features

- Extracts titles from front matter
- Generates sorted file lists
- Preserves existing documentation content
- Reports changes clearly
- Supports UTF-8 encoding for international documentation

### Example Output

```
✓ Updated: tutorial/migration/index.md (3 files listed)
✓ Updated: administrator-manual/provisioning/index.md (7 files listed)
  No changes: user-manual/index.md

Summary:
  Updated: 2
  Unchanged: 1
```

---

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
