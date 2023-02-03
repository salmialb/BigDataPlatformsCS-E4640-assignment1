import logging
from cassandra.cluster import Cluster


logging.basicConfig(level=logging.INFO)


def cassandra_connection():
    """
    Connection object for Cassandra
    :return: session, cluster
    """
    cluster = Cluster(['127.0.0.1'], port=9043)
    session = cluster.connect()
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS mysimbdp_coredms
        WITH REPLICATION =
        { 'class' : 'SimpleStrategy', 'replication_factor' : 3 }
        """)
    session.set_keyspace('mysimbdp_coredms')
    return session, cluster
def cassandra_create_tables():
    session, cluster = cassandra_connection()
    session.execute("DROP TABLE IF EXISTS covid")
    create_table =  "CREATE TABLE IF NOT EXISTS covid "\
                    "(date date"\
                    ", day int" \
                    ", month int"\
                    ", year int"\
                    ", deaths int"\
                    ", countriesAndTerritories text"\
                    ", geoId text"\
                    ", countryterritoryCode text"\
                    ", popData2019 int"\
                    ", continent text" \
                    ", cumulative_number_for_14_days_of_COVID_19_cases_per_100000 float"\
                    ", PRIMARY KEY(date))"
    logging.info("Creating table")
    session.execute(create_table)
                    
cassandra_create_tables()
if __name__ == "__main__":
    logging.info('Not callable')