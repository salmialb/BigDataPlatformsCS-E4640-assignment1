# Assignment Assignment_NR  Your_STUDENTID

> Guide line: This is the file where you will explain the structure of your assignment delivery. Remember to replace **Assignment_NR** with the number of the assignment (e.g., 1, 2, 3, or 4) and **Your_STUDENTID** with your student number. Remove all guidelines from the template.
1. run docker compose up
2. docker build -t mysimbdp-daas .
3.docker run -p 5000:5000 mysimbdp-daas

docker ps

docker exec -it code-mongodb1-1  bash
mongosh

rs.initiate({
   _id: "rs0",
   members: [
      { _id: 0, host: "mongodb1:27017" },
      { _id: 1, host: "mongodb2:27017" },
      { _id: 2, host: "mongodb3:27017" }
   ]
})