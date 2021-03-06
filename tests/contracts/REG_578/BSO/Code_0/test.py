from MainTest import MainTest



class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"REG-578 Проверить заполнение ответа при успешной загрузке заключенного договора ОСАГО (Type = BSO) (Errors.Code=0)"
        self.logger.info(f"# Start test {self.test_name}")
        self.PATH = r".\tests\contracts\REG_578\BSO\Code_0"
        self.REQUEST_FILE = r"NewContractRequest.json"
        self.RESPONSE_FILE = r"NewContractResponse.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsResponse"
        MainTest.__init__(self)
