import os
from datetime import datetime

# Get the correct paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
template_path = os.path.join(project_dir, 'template.md')
readme_path = os.path.join(project_dir, 'README.md')

# Process template
with open(template_path) as f:
    template = f.read()

content = template.replace("{{ date }}", datetime.now().strftime("%Y-%m-%d"))

# Write to README.md
with open(readme_path, 'w') as f:
    f.write(content)

print("✅ README updated successfully!")
print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}")