import pyarrow as pa
import pyarrow.parquet as pq
import duckdb

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