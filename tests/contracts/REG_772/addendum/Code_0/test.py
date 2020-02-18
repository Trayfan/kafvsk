from MainTest import MainTest


class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"REG-772 AccrualDate Загрузка даты начисления/возврата страховой премии (доп.соглашения)"
        self.logger.info(f"# Start test {self.test_name}")

        self.PATH = r".\tests\contracts\REG_772\addendum\Code_0"
        self.REQUEST_FILE = r"ChangeAddendumPremiumDateRequest.json"
        self.RESPONSE_FILE = r"ChangeAddendumPremiumDateResponse.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsResponse"
        MainTest.__init__(self)
