import glob
import re
import os

for filepath in glob.glob('_teaching/*.md'):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update front-matter
    if 'layout: page' in content:
        content = content.replace('layout: page', 'layout: course')

    # 2. Extract code and link
    kodu_match = re.search(r'class="badge bg-primary[^>]*>(.*?)</a>', content)
    link_match = re.search(r'href="(.*?)"[^>]*class="badge bg-primary', content)
    
    ders_kodu = kodu_match.group(1).strip() if kodu_match else ''
    ders_linki = link_match.group(1).strip() if link_match else ''
    
    # Insert into front matter
    if ders_kodu:
        content = re.sub(r'(---\nlayout: course\n)', f'\\1ders_kodu: "{ders_kodu}"\n', content)
    if ders_linki:
        content = re.sub(r'(---\nlayout: course\n(ders_kodu: .*\n)?)', f'\\1ders_linki: "{ders_linki}"\n', content)

    # 3. Extract and replace the big HTML block for "Dersin Amacı"
    # We will use regex to find the <div class="row mb-5"> ... </div> that contains "Dersin Amacı"
    block_match = re.search(r'<div class="row mb-5">.*?<h2[^>]*>Dersin Amacı</h2>\s*<p>(.*?)</p>\s*</div>\s*</div>', content, re.DOTALL)
    if block_match:
        amaci_text = block_match.group(1).strip()
        # Clean up inner html if any
        amaci_text = re.sub(r'\s+', ' ', amaci_text)
        replacement = f"## Dersin Amacı\n{amaci_text}\n"
        content = content[:block_match.start()] + replacement + content[block_match.end():]
    
    # 4. Remove all <hr class="my-5">
    content = re.sub(r'<hr class="my-5">\s*', '', content)

    # 5. Beautify the books section
    # Replace `<div class="card h-100 shadow-sm border-0 premium-teaching-card">` with `<a href="..." class="course-card">`
    # This is a bit complex via regex, maybe we can just let it be, or replace the class to use course-card
    content = content.replace('card h-100 shadow-sm border-0 premium-teaching-card', 'course-card')
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Processed all courses.")
