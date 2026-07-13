import pyarrow as pa
import pyarrow.parquet as pq
import duckdb
from abc import ABC, abstractmethod

'''
Big storage ting innit !
'''

class Storage(ABC):
	@abstractmethod
	def save(self, key, table): ...

	@abstractmethod
	def load(self, key): ...

class MemoryStorage(Storage):
	def __init__(self):
		self.data = {}

	def save(self, key, table):
		self.data[key] = table

	def load(self, key):
		return self.data[key]

class LocalStorage(Storage):
	def location(self, key):
		return f"{key}.parquet"

	def save(self, key, table):
		pq.write_table(table, self.location(key))

	def load(self, key):
		return pq.read_table(self.location(key))
