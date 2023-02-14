# This is a deployment/installation guide

It is a free form. you can use it to explain how to deploy/install and run  your code. Note that this deployment/installation guide ONLY helps to run your assignment. **It is not where you answer your solution for the assignment questions**

1. open up a terminal and cd to the code folder
2. run docker-compose up
3. open another terminal and run: docker exec -it code-mongodb1-1  mongo --eval "db.enableFreeMonitoring()" open the url for monitoring(cloud.mongodb.com/freemonitoring/cluster/XXXXXXXXXXXX)
4. in the same terminal run: docker exec -it code-mongodb1-1 bash
5. then type in the command: mongo
6. still in the same terminal run: 
    rs.initiate({
    _id: "rs0",
    members: [
        { _id: 0, host: "mongodb1:27017" },
        { _id: 1, host: "mongodb2:27017" },
        { _id: 2, host: "mongodb3:27017" }
    ]
    })
8. in a new terminal run  "python tests_multiple_tenants.py" to ingest the data
9. to have multiple tenants ingesting at once run  "python tests_multiple_tenants.py --mode tests --num_tenants n"  where n is the number of tenants you want simultaneously ingesting data.