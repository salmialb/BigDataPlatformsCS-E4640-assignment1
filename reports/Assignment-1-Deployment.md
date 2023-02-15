# This is a deployment/installation guide

It is a free form. you can use it to explain how to deploy/install and run  your code. Note that this deployment/installation guide ONLY helps to run your assignment. **It is not where you answer your solution for the assignment questions**

1. open up a terminal and cd to the code folder and run:
	
    
	docker-compose up -d
this will start up the mysimbdp-coredms & mysimbdp-dataingest components.
    
2. Initialize the replica sets bu running these commands:
    
        
    docker-compose exec configsvr01 sh -c "mongosh < /scripts/init-configserver.js"

    docker-compose exec shard01-a sh -c "mongosh < /scripts/init-shard01.js"
    docker-compose exec shard02-a sh -c "mongosh < /scripts/init-shard02.js"
    docker-compose exec shard03-a sh -c "mongosh < /scripts/init-shard03.js"
        
3. Initialize the router:
    docker-compose exec router01 sh -c "mongosh < /scripts/init-router.js"

5. Config sharding: 
    docker-compose exec router01 mongosh --port 27017
    
    sh.enableSharding("assignment1")

    db.adminCommand( { shardCollection: "assignment1.tortoise_data", key: { time: 1 } } )
    



6. in a new terminal run to ingest the data using 1 tenant


    "python ingestion_client.py" 

7. to have multiple tenants ingesting at once run:


    python ingestion_client.py --mode tests --num_tenants n
    (where n is the number of tenants you want simultaneously ingesting data. The test starts from 2 and will run up to n, adding 2 more per iteration)




