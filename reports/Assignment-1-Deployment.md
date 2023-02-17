# This is a deployment/installation guide

 ## 1. open up a terminal and cd to the code folder and run:
    cd code
    docker-compose up -d
## this will start up the mysimbdp-coredms & mysimbdp-dataingest components.
    
## 2. Initialize the replica sets bu running these commands:

    docker-compose exec configsvr01 sh -c "mongosh < /scripts/init-configserver.js"

    docker-compose exec shard01-a sh -c "mongosh < /scripts/init-shard01.js"
    docker-compose exec shard02-a sh -c "mongosh < /scripts/init-shard02.js"
    docker-compose exec shard03-a sh -c "mongosh < /scripts/init-shard03.js"
        
## 3. Initialize the router(might need to wait a few seconds after the previous command):
    docker-compose exec router01 sh -c "mongosh < /scripts/init-router.js"

## 5. Config sharding: 
    docker-compose exec router01 mongosh --port 27017
    
    sh.enableSharding("assignment1")

    db.adminCommand( { shardCollection: "assignment1.tortoise_data", key: { time: 1 } } )
    sh.status() <- check which shard is the primary one for monitoring



## 6. in a new terminal run to ingest the data using 1 tenant


    python mysimbdp-dataingest.py  --file data.csv

## 7. to have multiple tenants ingesting at once run:


    python mysimbdp-dataingest.py --mode tests --num_tenants 10 --file data.csv
    (where n is the number of tenants you want simultaneously ingesting data and file is the name of the file located in the data folder. The test starts from 1 and will run up to n, adding 1 more per iteration)

## 8. If you want to have monitoring:

    docker exec -it shard-01-node-a  mongosh --eval "db.enableFreeMonitoring()" <- put in the primary shard
## open the url. If you want to monitor another shard replace x in shard-x-node-a with 02 or 03.

## 9. To drop shards 
    docker-compose exec router01 mongosh --port 27017
    use assginment1
    db.adminCommand( { removeShard: "rs-shard-02" } )

    (This drops the 2nd shard for example)
## 10. Connecting with MongoDBCompass
    mongodb://127.0.0.1:27117,127.0.0.1:27118/