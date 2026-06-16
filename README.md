# Game Mod Video Hub

Game Mod Video Hub is an open-source catalog framework for documenting **game mod tutorial videos, installation walkthroughs, before-and-after showcases, creator notes, and review metadata**. It helps maintainers organize video references in a transparent and searchable format without hosting unsafe files or making unsupported claims.

The project is suitable for modding communities, documentation maintainers, and educators who want a consistent structure for linking to legitimate tutorials and explaining installation steps responsibly.

## Core Concepts

| Concept | Description |
|---|---|
| Video entry | A metadata page describing one tutorial, showcase, or walkthrough. |
| Mod profile | A short documentation page for a specific mod or tool. |
| Installation note | A safe, version-aware explanation of setup requirements. |
| Source reference | A link to an official page, creator channel, or release note. |

## Repository Structure

| Path | Purpose |
|---|---|
| `data/videos.json` | Example metadata records for tutorial and showcase videos. |
| `templates/video-entry.md` | Reusable Markdown template for new entries. |
| `docs/metadata-schema.md` | Field definitions for catalog records. |
| `assets/` | Optional thumbnails or diagrams with clear licensing. |

## Adding a Video Entry

A good video entry should include a clear title, game name, mod name, creator, source URL, publication date, supported version, and a short summary. The summary should describe what the viewer will learn without overpromising results.

## Safety and Quality Policy

This catalog should not link to piracy, malware, credential theft, game service abuse, account selling, or cheating tools. Modding content should respect game terms, creator licenses, and community safety expectations.

## Example Metadata

```json
{
  "title": "Installing a texture pack safely",
  "game": "Example Game",
  "mod_name": "Example Texture Pack",
  "creator": "Example Creator",
  "source_url": "https://example.com/video",
  "category": "installation-guide",
  "reviewed_at": "2026-06-16"
}
```

## Contributing

Contributions are welcome for metadata improvements, template refinements, documentation corrections, and accessibility notes. Each contribution should be factual and respectful of creators' rights.

## License

This project is released under the MIT License.
