# Assignment 1  100499799


This is my submission for the first assignment in the course Big Data Platforms (Aalto CS-E4640).
The project can be ran 100% locally using docker & docker-compose.

## Contents of repository:
### Code folder
   folder scripts: contains scripts for initializing up mysimbdp-coredms
   file docker.compose.yml: sets up mysimbdp-daas & mysimbdp-coredms
   file Dockerfile: build the web app that contains the API used to ingest data.
   file mysimbdp-daas.py: contains code for a REST API that handles ingestion of files
   file mysimbdp-datainget.py: Reads the data from data sources and calls the API in mysimbdp-daas to ingest the file
   file requirements.txt: contains the required dependencies.
### Data folder
   Contains the data to be ingested
### Logs folder
   contains performance & git logs.
### Reports folder
   contains instructions on deployment & report on the design of the project. Also contains answers to the questions asked in the assignment description.
## References

   https://github.com/minhhungit/mongodb-cluster-docker-compose <- Sharding setup in the docker-compose.yml. Used to make delivery and setup easier. Helps automate a lot of the setup. 
   LICENSE: https://github.com/minhhungit/mongodb-cluster-docker-compose/blob/master/LICENSE

