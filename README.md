# Streaming application pipeline with Kafka and Cassandra


This repo shows building an example live data streaming with Apache Kafka, the streamed data are processed and pushed into a standalone Cassandra database. All our applications are on Docker containers, we have streamed the live bitcoin data from the coin ranking api. You can check [Coinranking.com](https://developers.coinranking.com/api/documentation) for more information in setting your account to try out the API.  

## Prerequisites
If you don't have Docker desktop install already, you can install application from [Docker](https://www.docker.com/).


### 1. Clone this repo

```bash
git clone https://github.com/yTek01/streaming-with-kafka-cassandra.git
```

### 2. Pull the images and start the containers. 
Run the docker-compose.yml to start all the containers with the command below. 

```bash
cd streaming-with-kafka-cassandra
docker-compose up -d
```

### 3. Create Kafka topic
```bash
docker exec -it <Kafka_container_name> /bin/sh
```

```bash
cd /opt/kafka_version/bin
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic messages
kafka-topics.sh --list --zookeeper zookeeper:2181
```

### 4. Create Cassandra database keyspace and table.
```bash
docker exec -it <container_name> cqlsh
```

```bash
CREATE KEYSPACE btc_keyspaces WITH REPLICATION={'class': 'SimpleStrategy', 'replication_factor': 1};
```

```bash
CREATE TABLE IF NOT EXISTS btc_keyspaces.bitcoin_info (
uuiid UUID, 
coinID TEXT,
symbol TEXT,
name TEXT,
color TEXT,
iconUrl TEXT, 
marketCap TEXT, 
price TEXT,
listedAt BIGINT,
tier INT,
change TEXT,
rank INT, 
sparkline list<text>, 
lowVolume BOOLEAN, 
coinrankingUrl TEXT, 
twenty4hvolume TEXT,
btcPrice TEXT, 
PRIMARY KEY((uuiid), name));
```

### 5. Start the Python streaming application
We are going to start our applications in this chronological order, the python consumer.py, and python producer.py. The consumer API will be wait for messages from the producer API. 

```bash
python consumer.py
```
#### Open another terminal window. 
```bash
python producer.py. 
```

### 6. Go into the Cassandra database to confirm that your data is in the Cassandra database. 
```bash
docker exec -it <container_name> cqlsh
```

```bash
select count(*) from btc_keyspaces.bitcoin_info;
```
