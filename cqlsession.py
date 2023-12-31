"""
Utilities to provide connection to Astra DB (and local Cassandra)
"""

import os
from dotenv import find_dotenv, load_dotenv
from cassandra.cluster import (
    Cluster,
)
from cassandra.auth import PlainTextAuthProvider

# this will climb the directory tree looking for the file
dotenv_file = find_dotenv('.env')
load_dotenv(dotenv_file, override=True)

ASTRA_DB_SECURE_BUNDLE_PATH = os.environ["ASTRA_DB_SECURE_BUNDLE_PATH"]
ASTRA_DB_CLIENT_ID = os.environ["ASTRA_DB_CLIENT_ID"]
ASTRA_DB_CLIENT_SECRET = os.environ["ASTRA_DB_CLIENT_SECRET"]
ASTRA_DB_APPLICATION_TOKEN = os.environ["ASTRA_DB_APPLICATION_TOKEN"]
ASTRA_DB_KEYSPACE = os.environ["ASTRA_DB_KEYSPACE"]
LOCAL_KEYSPACE = os.environ.get('LOCAL_KEYSPACE', 'cassio_tutorials')

def getCQLSession(mode='astra_db'):

    if mode == 'astra_db':
        cluster = Cluster(
            cloud={
                "secure_connect_bundle": ASTRA_DB_SECURE_BUNDLE_PATH,
            },
            auth_provider=PlainTextAuthProvider(
                ASTRA_DB_CLIENT_ID,
                ASTRA_DB_CLIENT_SECRET,
            ),
        )
        astraSession = cluster.connect()
        return astraSession
    elif mode == 'local':
        cluster = Cluster()
        localSession = cluster.connect()
        return localSession
    else:
        raise ValueError('Unknown CQL Session mode')

def getCQLKeyspace(mode='astra_db'):
    if mode == 'astra_db':
        return ASTRA_DB_KEYSPACE
    elif mode == 'local':
        return LOCAL_KEYSPACE
    else:
        raise ValueError('Unknown CQL Session mode')