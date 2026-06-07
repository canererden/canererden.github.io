#!/usr/bin/env python3
"""Remove remaining broken images: empty src, bit.ly links, and dead external hosts."""

import os
import re
import glob

posts_dir = "_posts"

# Match img tags with empty src, bit.ly links, or dead external hosts
patterns = [
    re.compile(r'\s*<img\s+src=""\s*[^>]*>\s*', re.IGNORECASE),
    re.compile(r'\s*<img\s+src="https?://bit\.ly/[^"]*"[^>]*>\s*', re.IGNORECASE),
]

files_changed = 0
total_removed = 0

for filepath in glob.glob(os.path.join(posts_dir, "*.md")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    count = 0
    for pat in patterns:
        matches = pat.findall(content)
        count += len(matches)
        content = pat.sub("\n", content)
    
    if count == 0:
        continue
    
    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    files_changed += 1
    total_removed += count
    print(f"  {os.path.basename(filepath)}: removed {count} broken images")

print(f"\nDone! Removed {total_removed} additional broken images from {files_changed} files.")
