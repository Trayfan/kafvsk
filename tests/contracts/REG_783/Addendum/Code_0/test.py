from MainTest import MainTest



class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"Проверить заполнение ответа при успешном вызове запроса на изменение статуса доп соглашения ОСАГО и еОСАГО (Type = Addendum) (Errors.Code=0)"
        self.logger.info(f"# Start test {self.test_name}")
        self.PATH = r".\tests\contracts\REG_783\Addendum\Code_0"
        self.REQUEST_FILE = r"ChangeAddendumStatusRequest.json"
        self.RESPONSE_FILE = r"ChangeAddendumStatusResponse.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsResponse"
        MainTest.__init__(self)
