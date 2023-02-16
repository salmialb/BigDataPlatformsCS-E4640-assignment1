import pymongo
from pymongo import MongoClient
import time, argparse
from multiprocessing import Process
import certifi
import logging
import requests
import logging
import json
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default='default', help='Set execution mode. "tests" will execute tests with multiple tenants')
    parser.add_argument('--num_tenants', type=int, default=10, help='How many tenants for the test')
    parser.add_argument('--file', type=str, default="dat.csv", help='name of the file to be ingested')
    return parser.parse_args()
args = parse_args()

def insert_data(csv):
    

    
    with open(csv, 'r', encoding='utf8') as f:
        r = requests.post('http://localhost:5000/ingestion', files={'file': f})

    return " "
if __name__ == '__main__':
    if args.mode == "default":
        print("Inserting data...")
        start_time = time.time()
        csv = f"..\data/{args.file}"
        insert_data(csv)
        end_time = time.time()
        print(f"It took {end_time-start_time} seconds for 1 tenant to insert their file. ")

    if args.mode == "tests":
            csv = f"..\data/{args.file}"

            #The number of tenants for the test
            num_tenants = args.num_tenants

            #print(f"Initiating tests for {num_tenants} tenants...")
            # Create N processes, each simulating a tenant injecting data
            start_time = time.time()
            processes = []
            for j in range(1, num_tenants+1):
                print(f"Initiating tests for {j} tenants...")
                for i in range(j):
                    process = Process(target=insert_data,args=(csv,))
                    processes.append(process)

                # Start all processes
                for process in processes:
                    process.start()

                # Wait for all processes to finish
                for process in processes:
                    process.join()
                processes.clear()
                end_time = time.time()
                print(f"It took {end_time-start_time} seconds for {j} tenants to insert their files. ")
