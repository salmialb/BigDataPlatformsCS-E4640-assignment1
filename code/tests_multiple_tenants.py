import pymongo
from pymongo import MongoClient
import time, argparse
from multiprocessing import Process
import certifi
import logging
import requests
import logging
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default='default', help='Set execution mode. "tests" will execute tests with multiple tenants')
    parser.add_argument('--num_tenants', type=int, default=10, help='How many tenants for the test')
    return parser.parse_args()
args = parse_args()

def insert_data(csv):
   # coll = db["tests"]
    

    start_time = time.time()
    with open(csv, 'r') as f:
        r = requests.post('http://localhost:5000/ingestion', files={'file': f})

    end_time = time.time()
   # print(f"Tenant {tenant_id} took {end_time - start_time} seconds to insert the file records")
if __name__ == '__main__':
    if args.mode == "default":
        print("Inserting data...")
        csv = "..\data/data.csv"
        insert_data(csv)
        
    if args.mode == "tests":
            #Smaller file for less waiting
            csv = "..\data/data-small.csv"

            #The number of tenants for the test
            num_tenants = args.num_tenants

            print(f"Initiating tests for {num_tenants} tenants...")
            # Create N processes, each simulating a tenant injecting data
            start_time = time.time()
            processes = []
            for i in range(num_tenants):
                process = Process(target=insert_data,args=(csv,))
                processes.append(process)

            # Start all processes
            for process in processes:
                process.start()

            # Wait for all processes to finish
            for process in processes:
                process.join()
            end_time = time.time()
            print(f"It took {end_time-start_time} seconds for {num_tenants} tenants to insert their files. ")
#TODO: sharding