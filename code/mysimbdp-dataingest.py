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


@app.route('/ingestion', methods=['POST'])
def ingestion():

    db = get_db()
    coll = db['tortoise_data']
    file = request.files['file']
    file.save('data.csv')
    data = pd.read_csv("data.csv")
    coll.insert_many(data.to_dict('records'))    
    return " "


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

