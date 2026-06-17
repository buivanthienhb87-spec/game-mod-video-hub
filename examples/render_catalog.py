import json
from pathlib import Path

items = json.loads(Path('data/videos.json').read_text(encoding='utf-8'))
for item in items:
    print(f"- {item['title']} ({item['category']})")
