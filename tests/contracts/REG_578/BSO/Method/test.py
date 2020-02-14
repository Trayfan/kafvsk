from MainTest import MainTest




class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"Проверить заполнение ответа при указании невалидного значения атрибута Method (Errors.Code=1)"
        self.logger.info(f"# Start test {self.test_name}")

        
        self.PATH = r".\tests\contracts\REG_578\BSO\Method"
        self.REQUEST_FILE = r"NewContractRequest.json"
        self.RESPONSE_FILE = r"NewContractResponse.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsRequest"
        MainTest.__init__(self)
