#!/usr/bin/env python3
"""Replace broken vgy.me image links with a clean placeholder approach.

Strategy: Remove all <img src="https://i.vgy.me/..."> tags entirely.
These were screenshots of AI tool interfaces that are now broken.
The blog posts still have the text descriptions and links to the tools,
so removing the broken images makes the posts cleaner.
"""

import os
import re
import glob

posts_dir = "_posts"
pattern = re.compile(
    r'\s*<img\s+src="https://i\.vgy\.me/[^"]*"[^>]*>\s*',
    re.IGNORECASE
)

# Also clean up empty <p> or <div> wrappers that contained only the image
empty_wrapper = re.compile(r'<(p|div)[^>]*>\s*</\1>', re.IGNORECASE)

files_changed = 0
total_removed = 0

for filepath in glob.glob(os.path.join(posts_dir, "*.md")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "i.vgy.me" not in content:
        continue
    
    count = len(pattern.findall(content))
    if count == 0:
        continue
    
    new_content = pattern.sub("\n", content)
    # Clean up any resulting empty wrappers
    new_content = empty_wrapper.sub("", new_content)
    # Clean up multiple blank lines
    new_content = re.sub(r'\n{3,}', '\n\n', new_content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    files_changed += 1
    total_removed += count
    print(f"  {os.path.basename(filepath)}: removed {count} broken images")

print(f"\nDone! Removed {total_removed} broken vgy.me images from {files_changed} files.")
