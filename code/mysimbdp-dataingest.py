from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient
import csv,logging
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
    coll = db['covid_data']
    file = request.files['file']
    file.save('data.csv')
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        
        # Insert each row into MongoDB

        for row in reader:
            coll.insert_one(row)
          
 
        
    return "Successfully stored file!"


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

    #TODO: Why doesn't tests suddenly work?? 