import json
from datetime import datetime
from rest_api_script import data_from_coins_api
from kafka import KafkaProducer


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    while True:
        api_data = data_from_coins_api()
        print(f'Producing message @ {datetime.now()} | Message = {str(api_data)}')
        producer.send('messages', api_data)
