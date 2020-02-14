from kafka import KafkaProducer
from kafka import KafkaConsumer
import json

class kafka:
    def __init__(self):
        self.settings = self.__get_settings()
        self.ip = self.settings["kafka"]["ip"]
        self.port = self.settings["kafka"]["port"]
        self.api_version = (2, 2, 0)
        print("# Load settings")
        self.producer = self.__get_producer()
        self.consumer = self.__get_consumer()
        print("# Open connection")

    def __get_settings(self):
        try:
            return json.loads(open('settings.json', 'r').read())
        except Exception as err:
            print(f"Error! __get_settings: {err}")

    def __get_producer(self):
        try:
            return KafkaProducer(
                bootstrap_servers=[f"{self.ip}:{self.port}"], 
                api_version=self.api_version,
                value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        except Exception as err:
            print(f"Error! __get_producer: {err}")
            return None

    def __get_consumer(self):
        try:
            return KafkaConsumer(
                bootstrap_servers=[f"{self.ip}:{self.port}"],
                api_version=self.api_version,
                value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                consumer_timeout_ms=10000)
        except Exception as err:
            print(f"Error! __get_consumer: {err}")
            return None

    def send_msg(self, topic, msg):
        print("# Send message")
        try:
            self.producer.send(topic=topic, value=msg, partition=0)
        except Exception as err:
            print(f"Error! __send_msg: {err}")

    def close_connection(self):
        try:
            self.producer.close()
        except AttributeError:
            pass
        try:
            self.consumer.close()
        except AttributeError:
            pass
        print("Connections closed!")

    def get_msg(self, topic):
        print("# Start listening")
        try:
            self.consumer.subscribe([topic])
            msg = next(self.consumer)
            self.consumer.unsubscribe()
            return msg
        except Exception as err:
            print(f"Error! __get_msg: {err}")
            return None


