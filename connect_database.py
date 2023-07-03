from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
  'secure_connect_bundle': '/Users/samuel.matioli/work/langchain-astra/secure-connect-astravectordb.zip'
}
auth_provider = PlainTextAuthProvider('XxTDXuHdCsmQftbZELQGJJXW', 'cYz6FFkIPmESmQ.PESFSR6qCjfuF4FJ1v.ZpZAmdp-5it.z9YaZoHE,BD0OGgmXowHgsnv28G6AJ8_tn9wrdikLZnxYiB3MiweCopCcno+3tM3AdWX5rKqhUdGqUMF3a')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")