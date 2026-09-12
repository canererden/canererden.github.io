#!/usr/bin/env python3
import requests
import json
import re
import os

ORCID_ID = "0000-0002-7311-862X"
BIB_FILE = "_bibliography/papers.bib"

def get_existing_dois():
    if not os.path.exists(BIB_FILE):
        return set()
    
    with open(BIB_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple regex to find doi fields
    # Matches: doi = {10.something} or doi={10.something}
    dois = re.findall(r'doi\s*=\s*[\{"](10\.[^\}"]+)[\}"]', content, re.IGNORECASE)
    # also extract from url fields just in case: url = {https://doi.org/10...}
    urls = re.findall(r'url\s*=\s*[\{"]https?://doi\.org/(10\.[^\}"]+)[\}"]', content, re.IGNORECASE)
    
    all_dois = set(d.lower() for d in dois + urls)
    return all_dois

def get_orcid_works():
    url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch ORCID: {response.status_code}")
        return []
    
    data = response.json()
    dois = []
    
    for group in data.get("group", []):
        for work_summary in group.get("work-summary", []):
            ext_ids = work_summary.get("external-ids", {}).get("external-id", [])
            for ext_id in ext_ids:
                if ext_id.get("external-id-type") == "doi":
                    doi_val = ext_id.get("external-id-value")
                    if doi_val:
                        dois.append(doi_val.lower())
                        break # Only need one DOI per work
    return list(set(dois))

def get_bibtex_from_doi(doi):
    url = f"https://doi.org/{doi}"
    headers = {"Accept": "application/x-bibtex"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    
    # Fallback to crossref api
    crossref_url = f"https://api.crossref.org/works/{doi}/transform/application/x-bibtex"
    response = requests.get(crossref_url)
    if response.status_code == 200:
        return response.text
        
    print(f"Failed to fetch BibTeX for DOI: {doi}")
    return None

# Citation keys must be a single bare token. Crossref sometimes returns a key
# built from the title, which then carries commas and spaces and produces an
# entry that no BibTeX parser can read. Entries without a title or an author
# are almost always bad metadata rather than a real publication, so they are
# rejected instead of being appended to the bibliography.
KEY_SAFE = re.compile(r"[^A-Za-z0-9_:\-.+/]")
# The citation key runs from "@type{" up to the first real "field=" pair.
FIRST_FIELD = re.compile(r"(\w+)\s*=\s*[{\"0-9]")


def sanitise_entry(bibtex):
    """Return (cleaned_entry, problem). problem is None when the entry is usable."""
    match = re.match(r"@(\w+)\s*\{(.*)$", bibtex, re.S)
    if not match:
        return None, "not a BibTeX entry"
    entry_type, rest = match.group(1), match.group(2)

    field = FIRST_FIELD.search(rest)
    if not field:
        return None, "no fields in the record"

    # Everything before the first field is the key, however many commas
    # Crossref crammed into it.
    key_region = rest[: field.start()].rstrip().rstrip(",")
    body = rest[field.start():]

    safe_key = KEY_SAFE.sub("_", key_region.strip()).rstrip("_")
    safe_key = re.sub(r"_{2,}", "_", safe_key)
    if not safe_key.strip("_"):
        return None, "empty citation key"
    if len(safe_key) > 60:
        safe_key = safe_key[:60].rstrip("_")

    if not re.search(r"\btitle\s*=", body, re.I):
        return None, "no title field in the Crossref record"
    if not re.search(r"\bauthor\s*=", body, re.I):
        return None, "no author field in the Crossref record"

    return f"@{entry_type}{{{safe_key}, {body}", None


def main():
    print(f"Fetching existing DOIs from {BIB_FILE}...")
    existing_dois = get_existing_dois()
    print(f"Found {len(existing_dois)} existing DOIs.")

    print(f"Fetching works from ORCID ({ORCID_ID})...")
    orcid_dois = get_orcid_works()
    print(f"Found {len(orcid_dois)} DOIs on ORCID.")

    new_dois = [d for d in orcid_dois if d not in existing_dois]
    print(f"Found {len(new_dois)} new DOIs to fetch.")

    if not new_dois:
        print("No new publications to add.")
        return

    new_bibtex_entries = []
    rejected = []
    for i, doi in enumerate(new_dois, 1):
        print(f"[{i}/{len(new_dois)}] Fetching BibTeX for {doi}...")
        bibtex = get_bibtex_from_doi(doi)
        if not bibtex:
            rejected.append((doi, "no BibTeX returned"))
            continue
        cleaned, problem = sanitise_entry(bibtex.strip())
        if problem:
            print(f"    skipped: {problem}")
            rejected.append((doi, problem))
            continue
        new_bibtex_entries.append(cleaned)

    if rejected:
        print("\nThe following DOIs were skipped and need to be added by hand:")
        for doi, why in rejected:
            print(f"  {doi} - {why}")

    if new_bibtex_entries:
        print(f"Appending {len(new_bibtex_entries)} new entries to {BIB_FILE}...")
        with open(BIB_FILE, "a", encoding="utf-8") as f:
            f.write("\n\n" + "\n\n".join(new_bibtex_entries) + "\n")
        print("Done!")
    else:
        print("Could not fetch any new BibTeX entries.")

if __name__ == "__main__":
    main()
