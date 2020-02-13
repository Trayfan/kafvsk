from KafkaFramework import kafka
from json import loads
import os
from threading import Thread


class MainTest:
    def __init__(self):
        self.request_data = loads(open(os.path.join(self.PATH, self.REQUEST_FILE), 'r', encoding='utf8').read())
        self.response_data = loads(open(os.path.join(self.PATH, self.RESPONSE_FILE), 'r', encoding='utf8').read())

    def run_consumer(self, kf):
        msg = kf.get_msg(topic=self.response_topic)
        print(msg)

    def run_producer(self, kf, msg):
        kf.send_msg(topic=self.request_topic, msg=msg)

    def test(self):
        kf = kafka()
        thread1 = Thread(target=self.run_consumer, args=(kf,))
        thread2 = Thread(target=self.run_producer, args=(kf, self.request_data))
        #thread1.start()
        thread2.start()
        #thread1.join()
        thread2.join()
        # kf.send_to_contracts(request_data)