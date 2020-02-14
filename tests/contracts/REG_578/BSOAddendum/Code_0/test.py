from MainTest import MainTest




class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"Проверить заполнение ответа при успешной загрузке заключенного доп.соглашения ОСАГО/eОСАГО (Type=BSOAddendum) (Errors.Code=0)"
        self.logger.info(f"# Start test {self.test_name}")

        
        self.PATH = r".\tests\contracts\REG_578\BSOAddendum\Code_0"
        self.REQUEST_FILE = r"NewAddendumRequest.json"
        self.RESPONSE_FILE = r"NewAddendumResponse.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsResponse"
        MainTest.__init__(self)
