import pymongo
from pymongo import MongoClient
import time
from multiprocessing import Process
import certifi
import logging
import mysimbdp_daas
import requests
def get_db():
    client = MongoClient(
    host = "mongodb1",port=27017
    )

    db = client["assignment1"]
    return db

# Function to simulate a tenant injecting data into MongoDB

def insert_data(tenant_id):
   # coll = db["tests"]

    start_time = time.time()
    for i in range(1000):
        data = {"tenant_id": tenant_id, "data": i}
        request = requests.post('http://localhost:5000/insert_data',json=data)
    end_time = time.time()

    print(f"Tenant {tenant_id} took {end_time - start_time} seconds to insert 1000 records")
if __name__ == '__main__':
    #The number of tenants for the test
    num_tenants =3
     # Create N processes, each simulating a tenant injecting data
    processes = []
    for i in range(num_tenants):
        process = Process(target=insert_data, args=(i,))
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
