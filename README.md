# shulker
portable minimal data lakehouse (soon)

## Why this exists
rebuilding the storage core of a data platform
from scratch to learn the internals of systems like Snowflake / Databricks

## Status
early, learning in public\
just a storage seam right now (save/load over Parquet, queried with DuckDB)

## Roadmap
just beginning 🥹

- [x] storage seam --> save/load over Parquet  <- we are here!
- [ ] storage interface --> swap local disk <-> S3 without touching query code
- [ ] table format --> snapshots, time travel, immutable files
- [ ] catalog & ACID --> atomic commits, safe concurrent writers
- [ ] query & ingestion --> the platform grows up

## Run it
```
uv sync
uv run python explore.py
```