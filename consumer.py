
import json
from kafka import KafkaConsumer
from cassandra.cluster import Cluster
from uuid import uuid1

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    cluster = Cluster(['127.0.0.1'], port = 9042)
    session = cluster.connect('btc_keyspaces')

    for message in consumer:
        btc_api_data = json.loads(message.value)
        
        try:
            for i in range(0, len(btc_api_data['data']["coins"])):
                session.execute(
                """
                INSERT INTO btc_keyspaces.bitcoin_info (uuiid, coinID, symbol, name, color, iconUrl, marketCap, price, 
                listedAt, tier, change, rank, sparkline, lowVolume, coinrankingUrl, twenty4hvolume, btcPrice)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s , %s, %s, %s, %s )
                """,(uuid1(), btc_api_data['data']["coins"][i]["uuid"], btc_api_data['data']["coins"][i]["symbol"], 
                btc_api_data['data']["coins"][i]["name"], btc_api_data['data']["coins"][i]["color"], 
                btc_api_data['data']["coins"][i]["iconUrl"], btc_api_data['data']["coins"][i]["marketCap"],
                btc_api_data['data']["coins"][i]["price"], btc_api_data['data']["coins"][i]["listedAt"], 
                btc_api_data['data']["coins"][i]["tier"], btc_api_data['data']["coins"][i]["change"], 
                btc_api_data['data']["coins"][i]["rank"], btc_api_data['data']["coins"][i]["sparkline"], 
                btc_api_data['data']["coins"][i]["lowVolume"], btc_api_data['data']["coins"][i]["coinrankingUrl"], 
                btc_api_data['data']["coins"][i]["24hVolume"], btc_api_data['data']["coins"][i]["btcPrice"],
                )
                )
                print("Done Sending : ->",btc_api_data['data']["coins"][i])
        except:
            print("API Rate Limit Reached")
            pass
