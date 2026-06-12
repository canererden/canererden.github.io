import re

with open("scratch/medium_post.md", "r") as f:
    lines = f.readlines()

# Extract from line 14 onwards
# We will drop the "Markdown Content:" and medium headers
content = []
started = False
for i, line in enumerate(lines):
    if "Bu yazıda zaman serisi analizlerinde" in line:
        started = True
    
    if started:
        # Skip Jina AI / Medium artifacts
        if "Press enter or click to view image in full size" in line:
            continue
        if "Get Caner Erden’s stories in your inbox" in line:
            continue
        if "Join Medium for free to get updates from this writer." in line:
            continue
        if "Remember me for faster sign in" in line:
            continue
            
        content.append(line)

markdown_body = "".join(content)

front_matter = """---
layout: post
title: Zaman Serisi Tahminleri ve ARIMA Modelleri
date: 2020-05-06
giscus_comments: true
permalink: /2020/05/06/zaman-serisi-tahminleri-ve-arima-modelleri
tags:
  - zaman serisi
  - arima
  - tahmin
description: "Bu yazıda zaman serisi analizlerinde kullanılan tahmin çalışmalarından ve ARIMA modellerinden bahsedilecektir. Minitab üzerinde bir zaman serisi analizi uygulaması gerçekleştirilecektir."
---

"""

final_markdown = front_matter + markdown_body

with open("_posts/2020-05-06-zaman-serisi-tahminleri-ve-arima-modelleri.md", "w") as f:
    f.write(final_markdown)

print("File written successfully.")
