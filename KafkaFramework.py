from kafka import KafkaProducer
from kafka import KafkaConsumer
import json


class kafka:    
    def __init__(self, cl):
        self.logger = cl
        self.settings = self.__get_settings()
        self.ip = self.settings["kafka"]["ip"]
        self.port = self.settings["kafka"]["port"]
        self.api_version = (2, 2, 0)
        self.logger.info('Load settings from settings.json')
        self.producer = self.__get_producer()
        self.logger.info('Connect producer')
        self.consumer = self.__get_consumer()
        self.logger.info('Connect consumer')

    def __get_settings(self):
        try:
            return json.loads(open('settings.json', 'r').read())
        except Exception as err:
            self.logger.error(f'"Error! __get_settings: {err}"')

    def __get_producer(self):
        try:
            return KafkaProducer(
                bootstrap_servers=[f"{self.ip}:{self.port}"], 
                api_version=self.api_version,
                value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        except Exception as err:
            self.logger.error(f"Error! __get_producer: {err}")
            return None

    def __get_consumer(self):
        try:
            return KafkaConsumer(
                bootstrap_servers=[f"{self.ip}:{self.port}"],
                api_version=self.api_version,
                value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                consumer_timeout_ms=10000)
        except Exception as err:
            self.logger.error("Error! __get_consumer: {err}")
            return None

    def send_msg(self, topic, msg):
        self.logger.info("# Send message")
        try:
            self.producer.send(
                topic=topic, 
                key=b"", 
                value=msg, 
                partition=0)
            self.logger.info(f"> Send msg: {msg}")
        except Exception as err:
            self.logger.error(f"Error! __send_msg: {err}")

    def close_connection(self):
        try:
            self.producer.close()
        except AttributeError:
            pass
        try:
            self.consumer.close()
        except AttributeError:
            pass
        self.logger.info("Connections closed!")

    def get_msg(self, topic):
        self.logger.info("# Start listening")
        try:
            self.consumer.subscribe([topic])
            msg = next(self.consumer).value
            self.consumer.unsubscribe()
            self.logger.info(f"> Get msg: {msg}")
            return msg
        except Exception as err:
            self.logger.error(f"Error! __get_msg: {err}")
            return None


