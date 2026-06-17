from game_mod_video_hub.schema import VideoEntry, normalize_category


def test_video_entry_is_complete():
    entry = VideoEntry("Install Guide", "Example Game", "Creator", "https://example.com", "installation", "2026-06-16")
    assert entry.is_complete()


def test_normalize_category():
    assert normalize_category(" Installation Guide ") == "installation-guide"
