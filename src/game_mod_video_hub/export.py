from __future__ import annotations
import json
from pathlib import Path
from .schema import VideoEntry

def export_catalog(entries: list[VideoEntry], output_path: str) -> None:
    data = [{"title": e.title, "game": e.game, "creator": e.creator, "source_url": e.source_url, "category": e.category, "reviewed_at": e.reviewed_at} for e in entries]
    Path(output_path).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def load_catalog(path: str) -> list[VideoEntry]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [VideoEntry(**item) for item in data]
