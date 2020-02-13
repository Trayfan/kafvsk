from KafkaFramework import kafka
from json import loads
import os
from threading import Thread

def run_consumer(kf):
    msg = kf.get_msg_from_kbm()
    print(msg)

def run_producer(kf, msg):
    kf.send_to_kbm(msg)

def test():

    PATH = r".\tests\kbm\REG_583_REG_820\get_kbm\person_1"
    REQUEST_FILE = r"GetKbmRequest.json"
    RESPONSE_FILE = r"GetKbmResponse.json"


    request_data = loads(open(os.path.join(PATH, REQUEST_FILE), 'r', encoding='utf8').read())
    response_data = loads(open(os.path.join(PATH, RESPONSE_FILE), 'r', encoding='utf8').read())
    kf = kafka()
    thread1 = Thread(target=run_consumer, args=(kf,))
    thread2 = Thread(target=run_producer, args=(kf, request_data))
    #thread1.start()
    thread2.start()
    #thread1.join()
    thread2.join()
    # kf.send_to_contracts(request_data)

