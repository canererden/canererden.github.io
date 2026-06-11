import os
import glob
import re

replacements = {
    "category: Lisans": "category: Undergraduate",
    "category: Yüksek Lisans": "category: Graduate",
    "Türkiye": "Turkey",
    "title: Veri Madenciliği": "title: Data Mining",
    "title: İstatistikte Bilgisayar Uygulamaları": "title: Computer Applications in Statistics",
    "title: Lojistik ve Tedarik Zinciri Yönetimi": "title: Logistics and Supply Chain Management",
    "title: Uluslararası Tedarik Zinciri": "title: International Supply Chain Management",
    "title: Üretim Yönetimi": "title: Production Management",
    "title: Yöneylem Araştırması": "title: Operations Research",
    "title: Olasılık ve İstatistik": "title: Probability and Statistics",
    "title: Benzetim": "title: Simulation",
    "display_categories: [Lisans, Yüksek Lisans]": "display_categories: [Undergraduate, Graduate]"
}

# Process teaching pages
for filepath in glob.glob('_teaching/*.md'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    for k, v in replacements.items():
        content = content.replace(k, v)
        
    with open(filepath, 'w') as f:
        f.write(content)

# Process the main teaching page
teaching_main = "_pages/teaching.md"
with open(teaching_main, 'r') as f:
    content = f.read()
for k, v in replacements.items():
    content = content.replace(k, v)
with open(teaching_main, 'w') as f:
    f.write(content)

print("Teaching files translated successfully.")
