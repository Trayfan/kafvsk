from KafkaFramework import kafka
from json import loads
import os
from threading import Thread
from time import sleep
import queue
import customLogger as cl


class MainTest:
    def __init__(self):
        self.request_data = loads(open(os.path.join(self.PATH, self.REQUEST_FILE), 'r', encoding='utf8').read())
        self.response_data = loads(open(os.path.join(self.PATH, self.RESPONSE_FILE), 'r', encoding='utf8').read())


    def check_expected_actual(self, expected_result, actual_result):
        if expected_result == actual_result:
            self.logger.critical("Test pass!")
        else:
            self.logger.critical("Test failed!")

    def run_consumer(self, kf, TicketId, consumer_result):
        msg = kf.get_msg(topic=self.response_topic)
        if msg:
            try:
                if msg['SysInfo']['TicketId'] != TicketId:
                    self.logger.warning(f"Find wrong message. {msg['SysInfo']['TicketId']} != {TicketId}")
                    self.run_consumer(kf, TicketId)
                else:
                    consumer_result.append(msg)
            except Exception as err:
                self.logger.error(f"# Error run_consumer: {err}")

    def run_producer(self, kf, msg):
        sleep(1)
        kf.send_msg(topic=self.request_topic, msg=msg)

    def test(self):
        kf = kafka(cl=self.logger)
        consumer_result = []
        consumer_thread = Thread(target=self.run_consumer, args=(kf, self.request_data['SysInfo']['TicketId'], consumer_result))
        producer_thread = Thread(target=self.run_producer, args=(kf, self.request_data))
        consumer_thread.start()
        producer_thread.start()
        consumer_thread.join()
        producer_thread.join()
        if consumer_result:
            self.check_expected_actual(expected_result=self.response_data, actual_result=consumer_result[0])
        else:
            self.logger.info("Don't have an actual result!")
        kf.close_connection()