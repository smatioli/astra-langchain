# from cassandra.cluster import Cluster
# from cassandra.auth import PlainTextAuthProvider
# import os

# cloud_config= {
#   'secure_connect_bundle': os.environ.get('ASTRA_DB_SECURE_BUNDLE_PATH')
# }
# auth_provider = PlainTextAuthProvider(os.environ.get('ASTRA_DB_CLIENT_ID'), os.environ.get('ASTRA_DB_CLIENT_SECRET'))
# cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
# session = cluster.connect()

# row = session.execute("select release_version from system.local").one()
# if row:
#   print(row[0])
# else:
#   print("An error occurred.")