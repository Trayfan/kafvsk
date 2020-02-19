from MainTest import MainTest




class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"REG-578 Проверить заполнение ответа при успешной загрузке проекта договора ОСАГО/eОСАГО (Type=DraftContractForClosing) (Errors.Code=0)"
        self.logger.info(f"# Start test {self.test_name}")

        
        self.PATH = r".\tests\contracts\REG_578\DraftContractForClosing\Code_0"
        self.REQUEST_FILE = r"DraftContractRequest-ReadyForClosing.json"
        self.RESPONSE_FILE = r"DraftContractResponse-ReadyForClosing.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsResponse"
        MainTest.__init__(self)
