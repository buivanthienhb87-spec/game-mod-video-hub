# Data Schema

This document defines the recommended metadata fields used by the project. The schema is intentionally simple so contributors can add content without specialized tooling.

| Field | Type | Description |
|---|---|---|
| `title` | string | Human-readable page or item title. |
| `slug` | string | Lowercase URL-safe identifier. |
| `category` | string | Primary content category. |
| `summary` | string | Short factual summary for listings and search previews. |
| `source_url` | string | Official or verifiable reference link, when applicable. |
| `updated_at` | string | ISO date for the latest content review. |
| `tags` | array | Small set of natural tags for filtering. |
