from MainTest import MainTest



class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"REG-783 Проверить заполнение ответа при указании невалидиного значения атрибута Method (Errors.Code=1)"
        self.logger.info(f"# Start test {self.test_name}")
        self.PATH = r".\tests\contracts\REG_783\Addendum\Method"
        self.REQUEST_FILE = r"ChangeAddendumStatusRequest-invalidMethod.json"
        self.RESPONSE_FILE = r"ChangeAddendumStatusResponse-invalidMethod.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsResponse"
        MainTest.__init__(self)
