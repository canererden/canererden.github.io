import os
import glob
import re

for filepath in glob.glob('_posts/*.md'):
    with open(filepath, 'r') as f:
        content = f.read()

    # Split frontmatter
    parts = content.split('---')
    if len(parts) >= 3:
        frontmatter = parts[1]
        
        # Add thumbnail if not present
        if 'thumbnail:' not in frontmatter:
            # Insert before the first 'tags:' or at the end of frontmatter
            if 'tags:' in frontmatter:
                frontmatter = frontmatter.replace('tags:', 'thumbnail: assets/img/blog/default.jpg\ntags:')
            else:
                frontmatter += 'thumbnail: assets/img/blog/default.jpg\n'
                
        # We can also add a placeholder description if not present
        if 'description:' not in frontmatter:
            # extract first paragraph after frontmatter
            body = parts[2].strip()
            # remove markdown headers
            body_lines = [line for line in body.split('\n') if not line.startswith('#') and line.strip() != '']
            if body_lines:
                first_p = body_lines[0][:150].replace('"', "'") + "..."
                frontmatter += f'description: "{first_p}"\n'

        parts[1] = frontmatter
        new_content = '---'.join(parts)
        
        with open(filepath, 'w') as f:
            f.write(new_content)

print("Updated 15 blog posts.")
