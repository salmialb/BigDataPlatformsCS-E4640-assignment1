import logging
from cassandra.cluster import Cluster
import socket
import os
from cassandra.auth import PlainTextAuthProvider
import pandas
logging.basicConfig(level=logging.INFO)

def isOpen(ip, port):
   test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      test.connect((ip, int(port)))
      test.shutdown(1)
      return True
   except:
      return False

def fakeLoadBalancer():
    ips = []
    port = 9042
    for ip in os.environ.get('CASSANDRA_SEEDS').split(','):
        if isOpen(ip, port):
            ips.append(ip)
    return ips
def cassandra_connection(ips):
    """
    Connection object for Cassandra
    :return: session, cluster
    """
    cluster = Cluster(ips, port=9042, auth_provider=PlainTextAuthProvider(username='cassandra',password='cassandra'))
    session = cluster.connect()
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS mysimbdp_coredms
        WITH REPLICATION =
        { 'class' : 'SimpleStrategy', 'replication_factor' : 3 }
        """)
    session.set_keyspace('mysimbdp_coredms')
    return session, cluster
def cassandra_create_tables(session,cluster):
    
    create_table =  "CREATE TABLE IF NOT EXISTS covid "\
                    "(dateRep date"\
                    ", day int" \
                    ", month int"\
                    ", year int"\
                    ", cases int"\
                    ", deaths int"\
                    ", countriesAndTerritories text"\
                    ", geoId text"\
                    ", countryterritoryCode text"\
                    ", popData2019 int"\
                    ", continentExp text" \
                    ", Cumulative_number_for_14_days_of_COVID19_cases_per_100000 float"\
                    ", PRIMARY KEY(dateRep))"
    logging.info("Creating table...")
    session.execute(create_table)
    result = session.execute("SELECT * FROM mysimbdp_coredms.covid")
    print(result)
    return result

if __name__ == "__main__":
    logging.info('Not callable')