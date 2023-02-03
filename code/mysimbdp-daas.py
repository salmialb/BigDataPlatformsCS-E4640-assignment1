from flask import Flask, request
import cassandra
from cassandra.cluster import Cluster
import csv
app = Flask(__name__)


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
@app.route('/store_data', methods=['POST'])
def store_data():
    session, cluster =  cassandra_connection()
    data = request.get_json()
    # insert the data into Cassandra using CQL
    session.execute("INSERT INTO mysimbdp_coredms.covid (column1, column2, column3) VALUES ({}, {}, {})".format(data['column1'], data['column2'], data['column3']))
    return 'Data stored successfully'

@app.route('/get_data', methods=['GET'])
def get_data():
    session, cluster =  cassandra_connection()
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

    ##TODO: why connection refused?