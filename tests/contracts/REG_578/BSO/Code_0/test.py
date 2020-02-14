from MainTest import MainTest
import customLogger as cl



class Test_sub(MainTest):
    def __init__(self):
        self.logger = cl.custom_logger()
        self.test_name = r"Проверить заполнение ответа при успешной загрузке заключенного договора ОСАГО (Type = BSO) (Errors.Code=0)"
        self.logger.info(f"# Start test {self.test_name}")
        self.PATH = r".tests\contracts\REG_578\BSO\Code_0"
        self.REQUEST_FILE = r"NewContractRequest.json"
        self.RESPONSE_FILE = r"NewContractResponse.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsRequest"
        MainTest.__init__(self)
