from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient
import csv,logging
import pandas as pd
import json
app = Flask(__name__)

def get_db():
    client = MongoClient(
    host = "mongodb1",port=27017
    )

    db = client["assignment1"]
    return db
@app.route('/insert_data', methods=['POST'])
def insert_data():
    db = get_db()
    coll = db['tests']
    coll.insert_one(request.json)
    return "Successfully stored file!"

@app.route('/ingestion', methods=['POST'])
def ingestion():

    db = get_db()
    coll = db['tortoise_data']
    file = request.files['file']
    file.save('data.csv')
    data = pd.read_csv("data.csv")
   # with open("data.csv", "r") as file:
    #    reader = csv.DictReader(file, dialect = 'excel')
        
        # Insert each row into MongoDB

        #coll.insert_many(reader)   #for row in reader:
    coll.insert_many(data.to_dict('records'))
          
 
        
    return "Successfully stored file!"


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

    #TODO: Why doesn't tests suddenly work?? 