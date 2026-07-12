import pyarrow as pa
import pyarrow.parquet as pq
import duckdb
from abc import ABC, abstractmethod
'''
def location(key):
    return f"{key}.parquet"		# the ONLY place that knows where data lives

# 1. make a tiny table — you choose the rows
table = pa.table({"country": ["Turkiye", "Canada", "Syria", "Mongolia", "USA"], "clicks": [1453, 711867, 1282024, 1279, 741776]})

def save(key, table):
	return pq.write_table(table, location(key))

def load(key):
	return pq.read_table(location(key))


save("events", table)
events = load("events")

print(duckdb.sql("SELECT country, SUM(clicks) FROM events GROUP BY country"))
'''

example = pa.table({"country": ["Turkiye", "Canada", "Syria", "Mongolia", "USA"], "clicks": [1453, 711867, 1282024, 1279, 741776]})

class Storage(ABC):
	@abstractmethod
	def save(self, key, table): ...

	@abstractmethod
	def load(self, key): ...


class LocalStorage(Storage):
	def location(self, key):
		return f"{key}.parquet"

	def save(self, key, table):
		pq.write_table(table, self.location(key))

	def load(self, key):
		return pq.read_table(self.location(key))

class MemoryStorage(Storage):
	def __init__(self):
		self.data = {}

	def save(self, key, table):
		self.data[key] = table

	def load(self, key):
		return self.data[key]

storage = MemoryStorage()
storage.save("events", example)
events = storage.load("events")
print(duckdb.sql("SELECT country, SUM(clicks) FROM events GROUP BY country"))

