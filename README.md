# shulker
portable minimal data lakehouse (soon)

## Why this exists
rebuilding the storage core of a data platform
from scratch to learn the internals of systems like Snowflake / Databricks

## Status
early, learning in public\
simple storage interface complete

## Roadmap
learning more!

- [x] storage seam --> save/load over Parquet  <- we are here!
- [x] storage interface --> swap backends without touching query code
- [ ] S3 backend --> same interface but data lives in the cloud!
- [ ] table format --> snapshots, time travel, immutable files
- [ ] catalog & ACID --> atomic commits, safe concurrent writers
- [ ] query & ingestion --> the platform grows up

## Run it
```
uv sync
uv run python explore.py
```
