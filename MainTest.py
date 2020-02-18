from KafkaFramework import kafka
from json import loads, dump
import os
# from threading import Thread
from time import sleep
# import queue
import customLogger as cl
import uuid


class MainTest:
    def __init__(self):
        self.request_data = loads(open(os.path.join(self.PATH, self.REQUEST_FILE), 'r', encoding='utf8').read())
        self.response_data = loads(open(os.path.join(self.PATH, self.RESPONSE_FILE), 'r', encoding='utf8').read())

    def ordered(self, obj):
        if isinstance(obj, dict):
            return sorted((k, self.ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(self.ordered(x) for x in obj)
        else:
            return obj

    def check_expected_actual(self, expected_result, actual_result):
        del expected_result['SysInfo']['TimeStamp']
        try:
            del actual_result['SysInfo']['TimeStamp']
        except KeyError:
            self.logger.critical("# Test failed! Wrong actual result.")
            return 0
        try:
            if self.ordered(actual_result) == self.ordered(expected_result):
                self.logger.info("# Test pass!")
            else:
                self.logger.critical("# Test failed! Expected result != Actual result.")
        except Exception as err:
            self.logger.warning(f"ERROR check_expected_actual: Не получилось проверить первым методом, пробуем второй. {err}")
            if actual_result == expected_result:
                self.logger.info("# Test pass!")
            else:
                self.logger.critical("# Test failed! Expected result != Actual result.")

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

    def get_correlation_id(self):
        return bytes(str(uuid.uuid1()), encoding='utf8')

    def test(self):
        kf = kafka(cl=self.logger)
        consumer_result = []
        correlation_id = self.get_correlation_id()
        kf.send_msg(topic=self.request_topic, msg=self.request_data, correlation_id=correlation_id)
        msg = kf.get_msg(topic=self.response_topic, correlation_id=correlation_id)
        with open(os.path.join(self.PATH, "RESPONSE.json"), 'w', encoding='utf-8') as file:
            dump(msg, file, ensure_ascii=False)
        if msg:
            self.check_expected_actual(expected_result=self.response_data, actual_result=msg)
        else:
            self.logger.info("Don't have an actual result!")
        kf.close_connection()
