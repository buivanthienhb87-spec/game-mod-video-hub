from game_mod_video_hub.schema import VideoEntry
from game_mod_video_hub.export import export_catalog, load_catalog
import tempfile, os

def test_roundtrip():
    entries = [VideoEntry("Guide", "Game", "Creator", "https://example.com", "installation", "2026-06-16")]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        export_catalog(entries, f.name)
        path = f.name
    loaded = load_catalog(path)
    os.unlink(path)
    assert loaded[0].title == "Guide"
