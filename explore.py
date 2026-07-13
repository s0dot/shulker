import pyarrow as pa
import pyarrow.parquet as pq
import duckdb
from abc import ABC, abstractmethod
from shulker.storage import LocalStorage, MemoryStorage
example = pa.table({"country": ["Turkiye", "Canada", "Syria", "Mongolia", "USA"], "clicks": [1453, 711867, 1282024, 1279, 741776]})

storage = MemoryStorage()
storage.save("events", example)
events = storage.load("events")
print(duckdb.sql("SELECT country, SUM(clicks) FROM events GROUP BY country"))

