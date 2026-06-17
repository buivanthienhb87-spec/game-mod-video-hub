from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class VideoEntry:
    title: str
    game: str
    creator: str
    source_url: str
    category: str
    reviewed_at: str

    def is_complete(self) -> bool:
        return all([self.title, self.game, self.creator, self.source_url, self.category, self.reviewed_at])


def normalize_category(value: str) -> str:
    return value.strip().lower().replace(" ", "-")
