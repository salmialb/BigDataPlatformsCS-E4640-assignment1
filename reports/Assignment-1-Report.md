# This your assignment report

It is a free form. you can add:

* your designs
* your answers to questions in the assignment
* your test results
* etc.

The best way is to have your report written in the form of point-to-point answering the assignment.
# Part  1
## Question 1
The application domain for mysimbdp-coredms is big data storage and management. The types of data to be supported can vary widely since I am using a NoSQL database, including structured and unstructured data, as well as text, images, and multimedia data. For the project I am only using one dataset -> one type of data as instructed.

For this platform, the technologies used are a Flask API and MongoDB. Flask is used for building the API for data ingestion, and MongoDB is used for storing and managing the data. A replica set cluster is used for high availability and to ensure that data is always available, even if a single node goes down.

This platform is well-suited for big data workloads under the following situations/assumptions:

    High data volume: The platform can handle large amounts of data and could potentially scale to meet the demands of a growing business.
    High data velocity: The platform can handle fast data ingestion rates, making it suitable for real-time and near real-time data processing.
    High data variety: The platform can store and manage a wide range of data types, including structured, semi-structured, and unstructured data.
    High data variability: The platform can handle rapidly changing data and adapt to changing data patterns.

## Question 2
    mysimbdp-dataingest: This component reads data from external data sources and then passes the data to the mysimbdp-coredms component using APIs.
    mysimbdp-coredms: This component acts as the main storage for the platform. It receives data from mysimbdp-dataingest, stores it, and makes it available to other components in the platform through APIs.
    mysimbdp-daas: This component acts as an intermediary between external data consumers and mysimbdp-coredms. It exposes APIs that allow external data consumers to access the data stored in mysimbdp-coredms.
    
    In terms of third-party services and infrastructures, mysimbdp will rely on external data sources for data ingestion and storage. Some common data sources can include file systems, databases, messaging systems, and cloud storage services. Additionally, mysimbdp may rely on third-party tools for data processing and analysis, such as Apache Spark or Apache Hadoop.
## Question 3
To prevent single-point-of-failure I set up a clster of nodes using replicasets in MongoDB. Replica sets provide automatic failover by maintaining multiple copies of data across multiple nodes, ensuring that if one node fails, the data remains available. I developed my project to work locally. In a real world scenario this would not be optimal and you would want to spread out the nodes on different machines.
## Question 4
My configuration is as follows:
1. One primary node responsible for handling all write operations
2. Two secondary nodes that maintain a copy of the data from the primary node and are available to handle read operationd and take over if the primary node fails.

## Question 5 
I would utilize the following strategies to allow scaling for a varying amount of tenants:

Horizontal scaling: I would increase the number of nodes in the cluster depending on the load in order to distribute the load on more nodes.
Load Balancing: Load balancing would optimize the distribution of requests ensuring that the all nodes get an equal amount of requests.
Sharding: Each shard would be a separate server, so each tenant's data would be stored on a separate shard, reducing the impact of one tenant's data on another. This would allow for better distribution of processing power and storage space across the cluster, allowing for more tenants to ingest data simultaneously without performance degradation. Additionally, sharding would also provide the ability to horizontally scale the platform by simply adding more shards to the cluster. As the number of tenants and the volume of data they store increases, new shards can be added to the cluster to handle the additional load.
Use of Queuing Systems: To handle spikes in data ingestion requests, you can use a queuing system such as RabbitMQ or Apache Kafka. This will store incoming data ingestion requests in a queue and process them in an orderly manner.
Use of Caching: To improve the performance of mysimbdp, you can use a caching mechanism to store frequently accessed data in memory. This will reduce the load on the database and improve the overall performance of the system.

Note that I'm not going to be implementing all of these since just isn't feasible for a school project given the constraints and my time limitation.

# Part 2
{ "_id" : ObjectId("63eb6e7bb49ae57e405fc77c"),
"dateRep" : "25/11/2020",
"day" : 25, 
"month" : 11, 
"year" : 2020,
"cases" : 185, 
"deaths" : 13,
"countriesAndTerritories" : "Afghanistan",
"geoId" : "AF",
"countryterritoryCode" : "AFG",
"popData2019" : 38041757, 
"continentExp" : "Asia", 
"Cumulative_number_for_14_days_of_COVID19_cases_per_100000" : 7.1999829 }