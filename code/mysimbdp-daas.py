from flask import Flask, request
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import socket
import csv
import os
app = Flask(__name__)
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

def cassandra_connection():
    """
    Connection object for Cassandra
    :return: session, cluster
    """
    cluster = Cluster(fakeLoadBalancer(), port=9042, auth_provider=PlainTextAuthProvider(username='cassandra',password='cassandra'))
    session = cluster.connect()
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS mysimbdp_coredms
        WITH REPLICATION =
        { 'class' : 'SimpleStrategy', 'replication_factor' : 3 }
        """)
    session.set_keyspace('mysimbdp_coredms')
    return session, cluster
    
@app.route('/store_data', methods=['POST'])
def store_data():
    
    session, cluster =  cassandra_connection()
    data = request.get_json()
    # insert the data into Cassandra using CQL
    session.execute("INSERT INTO mysimbdp_coredms.covid (column1, column2, column3) VALUES ({}, {}, {})".format(data['column1'], data['column2'], data['column3']))
    return 'Data stored successfully'

@app.route('/get_data', methods=['GET'])
def get_data():
    print("Aaa")
    session,cluster =cassandra_connection()
    
    # retrieve the data from Cassandra using CQL
    result = session.execute("SELECT * FROM mysimbdp_coredms.covid")
    return result

@app.route('/store_csv', methods=['POST'])
def store_csv():
    session, cluster =  cassandra_connection()
    file = request.files['file']
    file.save('data.csv')
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        # read the rows in the csv file and store them in Cassandra
        for row in reader:
            # insert the data into Cassandra using CQL
            session.execute("INSERT INTO mysimbdp_coredms.covid ({}) VALUES ({})".format(','.join(header), ','.join(row)))
    return 'CSV file stored successfully'
import setupDB

@app.route('/init_db', methods=['GET'])
def init_db():
    session,cluster = cassandra_connection()
    result = setupDB.cassandra_create_tables(session, cluster)
    
    # retrieve the data from Cassandra using CQL
    print("Creating table")
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)

    ##TODO: Use pandas to transform date column into yyyy-mm-dd. Currently is dd/mm/yy