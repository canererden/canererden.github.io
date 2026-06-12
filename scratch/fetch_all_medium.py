import urllib.request
import xml.etree.ElementTree as ET
import os
import re
from datetime import datetime
import glob

def simple_slugify(text):
    text = text.lower()
    # Replace turkish chars
    tr_map = {'ç': 'c', 'ğ': 'g', 'ı': 'i', 'i': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u'}
    for src, dst in tr_map.items():
        text = text.replace(src, dst)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

rss_url = "https://medium.com/@cerden/feed"
req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
data = response.read()
root = ET.fromstring(data)
items = root.findall('.//item')

posts_dir = "_posts"
os.makedirs(posts_dir, exist_ok=True)
existing_files = glob.glob(os.path.join(posts_dir, "*.md"))

for item in items:
    title = item.find('title').text
    link = item.find('link').text
    pubDate_str = item.find('pubDate').text
    
    # PubDate example: "Wed, 15 Feb 2023 09:06:01 GMT"
    # Parse to datetime
    pub_date = datetime.strptime(pubDate_str, "%a, %d %b %Y %H:%M:%S GMT")
    date_str = pub_date.strftime("%Y-%m-%d")
    year = pub_date.strftime("%Y")
    month = pub_date.strftime("%m")
    day = pub_date.strftime("%d")
    
    slug = simple_slugify(title)
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(posts_dir, filename)
    
    # Check if already exists (skip specific Zaman Serisi one since we already did it)
    if "zaman-serisi-tahminleri" in slug:
        print(f"Skipping {title} (already processed)")
        continue
        
    # Check if a file with similar title exists (e.g. harvard)
    file_exists = False
    for existing in existing_files:
        if slug in existing:
            file_exists = True
            break
            
    if file_exists or os.path.exists(filepath):
        print(f"Skipping {title} (file already exists)")
        continue

    print(f"Fetching: {title}")
    
    # Clean the link for jina (remove query parameters like ?source=rss...)
    clean_link = link.split("?")[0]
    jina_url = f"https://r.jina.ai/{clean_link}"
    
    try:
        j_req = urllib.request.Request(jina_url, headers={'User-Agent': 'Mozilla/5.0'})
        j_resp = urllib.request.urlopen(j_req)
        md_content = j_resp.read().decode('utf-8')
    except Exception as e:
        print(f"Failed to fetch {jina_url}: {e}")
        continue
        
    # Process markdown content
    lines = md_content.split('\n')
    content = []
    started = False
    description = ""
    
    for line in lines:
        if "Markdown Content:" in line:
            started = True
            continue
            
        if started:
            # Skip Jina/Medium artifacts
            if "Press enter or click to view image in full size" in line:
                continue
            if "Get Caner Erden’s stories in your inbox" in line:
                continue
            if "Join Medium for free to get updates from this writer." in line:
                continue
            if "Remember me for faster sign in" in line:
                continue
            if re.match(r'^\[!\[Image \d+: .*?\]\(.*?\)\].*$', line):
                continue
            if re.match(r'^\d+ min read$', line):
                continue
            # Also skip the date string at the beginning of the post body
            if re.match(r'^[A-Z][a-z]{2} \d{1,2}, \d{4}$', line):
                continue
                
            content.append(line)
            
            # Grab the first non-empty line as description
            if not description and line.strip() and not line.startswith('#') and not line.startswith('!['):
                description = line.strip()

    markdown_body = "\n".join(content).strip()
    
    permalink = f"/{year}/{month}/{day}/{slug}"
    
    front_matter = f"""---
layout: post
title: "{title.replace('"', '')}"
date: {date_str}
giscus_comments: true
permalink: {permalink}
tags:
  - blog
description: "{description[:150]}..."
---

"""

    final_markdown = front_matter + markdown_body
    
    with open(filepath, "w") as f:
        f.write(final_markdown)
        
    print(f"Successfully wrote {filepath}")
