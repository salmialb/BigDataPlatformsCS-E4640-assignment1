from flask import Flask, request
import pymongo
from pymongo import MongoClient
import pandas as pd
app = Flask(__name__)

def get_db():
    client = MongoClient("mongodb://router-01:27017/assignment1"   )
    db = client["assignment1"]
    return db


@app.route('/ingestion', methods=['POST'])
def ingestion():

    db = get_db()
    coll = db['tortoise_data']
    file = request.files['file']
    file.save('data.csv')
    data = pd.read_csv("data.csv")
    doc = coll.insert_many(data.to_dict('records')) 
       
    return len(doc)


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

