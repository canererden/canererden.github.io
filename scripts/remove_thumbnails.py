import glob

for filepath in glob.glob('_posts/*.md'):
    with open(filepath, 'r') as f:
        content = f.read()

    parts = content.split('---')
    if len(parts) >= 3:
        frontmatter = parts[1]
        
        # Remove thumbnail lines
        new_frontmatter_lines = []
        for line in frontmatter.split('\n'):
            if not line.startswith('thumbnail:'):
                new_frontmatter_lines.append(line)
        
        parts[1] = '\n'.join(new_frontmatter_lines)
        new_content = '---'.join(parts)
        
        with open(filepath, 'w') as f:
            f.write(new_content)

print("Removed thumbnails from all old blog posts.")
