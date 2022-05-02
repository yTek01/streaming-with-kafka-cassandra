CREATE KEYSPACE btc_keyspaces WITH REPLICATION={'class': 'SimpleStrategy', 'replication_factor': 1};

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
