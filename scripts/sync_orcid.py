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
    for i, doi in enumerate(new_dois, 1):
        print(f"[{i}/{len(new_dois)}] Fetching BibTeX for {doi}...")
        bibtex = get_bibtex_from_doi(doi)
        if bibtex:
            new_bibtex_entries.append(bibtex.strip())

    if new_bibtex_entries:
        print(f"Appending {len(new_bibtex_entries)} new entries to {BIB_FILE}...")
        with open(BIB_FILE, "a", encoding="utf-8") as f:
            f.write("\n\n" + "\n\n".join(new_bibtex_entries) + "\n")
        print("Done!")
    else:
        print("Could not fetch any new BibTeX entries.")

if __name__ == "__main__":
    main()
